"""
Countdown display configuration.
修士論文締め切りカウントダウンの設定
"""

import datetime
from dataclasses import dataclass
from typing import Tuple


@dataclass
class DeadlineConfig:
    """締め切り設定"""

    year: int = 2026
    month: int = 2
    day: int = 1
    hour: int = 17
    minute: int = 0
    second: int = 0

    @property
    def datetime(self) -> datetime.datetime:
        """datetime オブジェクトを返す"""
        return datetime.datetime(
            self.year, self.month, self.day, self.hour, self.minute, self.second
        )

    def __str__(self):
        return self.datetime.strftime("%Y-%m-%d %H:%M:%S")


@dataclass
class DisplayConfig:
    """表示設定"""

    normal_color: Tuple[int, int, int] = (255, 255, 255)  # 白
    rainbow_flash: bool = True
    flash_duration: float = 3.0
    blink_frequency: float = 5.0
    font_scale: float = 0.5
    font_thickness: int = 1
    text_format: str = "{hours}h{minutes:02d}m{seconds:02d}s"
    expired_text: str = "DONE!"
    warning_color: Tuple[int, int, int] = None
    warning_hours: int = 24


@dataclass
class SerialConfig:
    """シリアルポート設定"""

    port: str = None
    baudrate: int = 115200
    timeout: float = 1.0


@dataclass
class Config:
    """全体設定"""

    deadline: DeadlineConfig = None
    display: DisplayConfig = None
    serial: SerialConfig = None
    fps: float = 30.0
    panel_width: int = 128
    panel_height: int = 32

    def __post_init__(self):
        if self.deadline is None:
            self.deadline = DeadlineConfig()
        if self.display is None:
            self.display = DisplayConfig()
        if self.serial is None:
            self.serial = SerialConfig()


DEFAULT_CONFIG = Config()

THESIS_CONFIG = Config(
    deadline=DeadlineConfig(year=2026, month=2, day=1, hour=17, minute=0, second=0),
    display=DisplayConfig(
        normal_color=(255, 255, 255),
        rainbow_flash=True,
        flash_duration=3.0,
        blink_frequency=5.0,
        font_scale=0.5,
        font_thickness=1,
        warning_color=(255, 100, 0),
        warning_hours=24,
    ),
    serial=SerialConfig(
        port=None,
    ),
    fps=30.0,
)
