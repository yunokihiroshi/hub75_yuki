# Countdown Display Scripts

修士論文締め切りまでのカウントダウンを表示する独立したスクリプトシステム。

## ファイル構成

- `countdown_config.py` - 設定ファイル（締め切り、表示設定、シリアルポート設定）
- `countdown_display.py` - 実行スクリプト
- `README.md` - このファイル

## 使い方

### 基本的な使い方

```bash
cd application/scripts
python countdown_display.py
```

### オプション

```bash
# カスタムシリアルポートを指定
python countdown_display.py --port COM3

# 設定を変更（THESIS_CONFIG または DEFAULT_CONFIG）
python countdown_display.py --config THESIS_CONFIG

# フレームレートを変更
python countdown_display.py --fps 60

# ヘルプを表示
python countdown_display.py --help
```

## 設定のカスタマイズ

`countdown_config.py` を編集して設定をカスタマイズできます：

### DeadlineConfig（締め切り設定）

```python
DeadlineConfig(
    year=2026,
    month=2,
    day=1,
    hour=17,
    minute=0,
    second=0
)
```

### DisplayConfig（表示設定）

```python
DisplayConfig(
    normal_color=(255, 255, 255),  # 通常時の色（RGB）
    rainbow_flash=True,             # 虹色フラッシュを有効化
    flash_duration=3.0,             # フラッシュ時間（秒）
    blink_frequency=5.0,            # 点滅周波数（Hz）
    font_scale=0.5,                 # フォントサイズ
    font_thickness=1,               # フォント太さ
    warning_color=(255, 100, 0),    # 警告色（RGB）
    warning_hours=24,               # 警告時間（時間）
    text_format="{hours}h{minutes:02d}m{seconds:02d}s",  # 表示フォーマット
    expired_text="DONE!"            # 締め切り後のテキスト
)
```

### SerialConfig（シリアルポート設定）

```python
SerialConfig(
    port=None,        # シリアルポート（Noneで自動検出）
    baudrate=115200,  # ボーレート
    timeout=1.0       # タイムアウト（秒）
)
```

## 機能

- **リアルタイムカウントダウン**: 締め切りまでの残り時間を表示
- **虹色フラッシュ**: ちょうど○時間0分0秒のタイミングで虹色フラッシュを3秒間表示
- **警告表示**: 残り時間が24時間以下になると警告色で表示
- **カスタマイズ可能**: 設定ファイルで簡単にカスタマイズ可能

## 依存関係

- Python 3.9+
- numpy
- opencv-python
- pyserial

## トラブルシューティング

### シリアルポートが見つからない

```
❌ Error initializing controller: No serial device found.
```

解決方法：
1. USBケーブルが接続されているか確認
2. `--port` オプションで明示的にポートを指定
3. `python -m serial.tools.list_ports` でポートを確認

### 設定が見つからない

```
❌ Error: Config 'XXX' not found in countdown_config.py
```

解決方法：
- `countdown_config.py` に定義されている設定名を使用
- 利用可能な設定: `DEFAULT_CONFIG`, `THESIS_CONFIG`

## 開発者向け情報

### 新しい設定を追加

`countdown_config.py` に新しい `Config` オブジェクトを定義：

```python
MY_CUSTOM_CONFIG = Config(
    deadline=DeadlineConfig(
        year=2026,
        month=3,
        day=15,
        hour=12,
        minute=0,
        second=0
    ),
    display=DisplayConfig(
        normal_color=(0, 255, 0),
        rainbow_flash=False,
    ),
    fps=60.0,
)
```

使用方法：

```bash
python countdown_display.py --config MY_CUSTOM_CONFIG
```
