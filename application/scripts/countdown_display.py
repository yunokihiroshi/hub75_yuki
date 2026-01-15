#!/usr/bin/env python3
"""
Countdown display for thesis deadline.
Standalone script for continuous operation.

使い方:
  python countdown_display.py
  python countdown_display.py --port COM3
  python countdown_display.py --config THESIS_CONFIG
"""
import argparse
import sys
import time
from pathlib import Path

project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root / "src"))

from led_matrix_controller.controller import LEDMatrixController
from led_matrix_controller.devices import SerialDevice
import countdown_config


def main():
    parser = argparse.ArgumentParser(
        description="Thesis Deadline Countdown Display",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python countdown_display.py
  python countdown_display.py --port COM3
  python countdown_display.py --config THESIS_CONFIG
  python countdown_display.py --fps 60
        """,
    )
    parser.add_argument("--port", help="Serial port (auto-detect if not specified)")
    parser.add_argument(
        "--config", default="DEFAULT_CONFIG", help="Config name from countdown_config.py"
    )
    parser.add_argument("--fps", type=float, help="Frames per second (overrides config)")
    args = parser.parse_args()

    # Validate and get config (safer than arbitrary getattr)
    available_configs = {
        "DEFAULT_CONFIG": countdown_config.DEFAULT_CONFIG,
        "THESIS_CONFIG": countdown_config.THESIS_CONFIG,
    }

    if args.config not in available_configs:
        print(f"❌ Error: Config '{args.config}' not found in countdown_config.py")
        print(f"Available configs: {', '.join(available_configs.keys())}")
        sys.exit(1)

    config = available_configs[args.config]

    if args.port:
        config.serial.port = args.port
    if args.fps:
        config.fps = args.fps

    print("=" * 60)
    print("🎓 Thesis Deadline Countdown Display")
    print("=" * 60)
    print(f"📅 Deadline: {config.deadline}")
    print(f"⏰ Current:  {time.strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"🎨 Display:  {config.panel_width}x{config.panel_height} @ {config.fps} FPS")
    print(f"🔌 Port:     {config.serial.port or 'Auto-detect'}")
    print(f"🌈 Rainbow:  {'Enabled' if config.display.rainbow_flash else 'Disabled'}")
    print("=" * 60)
    print("Press Ctrl+C to stop")
    print()

    try:
        device = SerialDevice(
            port=config.serial.port, baudrate=config.serial.baudrate, timeout=config.serial.timeout
        )
        controller = LEDMatrixController(
            device=device, width=config.panel_width, height=config.panel_height
        )
        controller.connect()
    except Exception as e:
        print(f"❌ Error initializing controller: {e}")
        sys.exit(1)

    try:
        controller.run_countdown(config)
    except KeyboardInterrupt:
        print("\n\n⏹  Stopping countdown display...")
        controller.clear()
        print("✅ Stopped")
    finally:
        controller.disconnect()


if __name__ == "__main__":
    main()
