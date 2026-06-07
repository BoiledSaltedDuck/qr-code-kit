#!/usr/bin/env python3
"""
qr-code-kit - 二维码生成与解析工具
功能：生成二维码、批量生成、解析二维码
用法：qr-code encode [数据] [输出文件]
      qr-code decode [二维码图片]
"""
import sys
from pathlib import Path

try:
    import qrcode
    from qrcode.image.styledpil import StyledPilImage
    from qrcode.image.styles.moduledrawers import RoundedModuleDrawer
except ImportError:
    print("正在安装 qrcode...")
    import subprocess
    subprocess.check_call([sys.executable, "-m", "pip", "install", "qrcode[pil]", "-q"])
    import qrcode
    from qrcode.image.styledpil import StyledPilImage
    from qrcode.image.styles.moduledrawers import RoundedModuleDrawer

try:
    from pyzbar.pyzbar import decode as pyzbar_decode
    from PIL import Image
    HAS_PYZBAR = True
except ImportError:
    HAS_PYZBAR = False
    from PIL import Image


def encode(data, output_file, fill_color="black", back_color="white", with_logo=None):
    """生成二维码"""
    try:
        qr = qrcode.QRCode(
            version=None,
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            box_size=10,
            border=4,
        )
        qr.add_data(data)
        qr.make(fit=True)

        img = qr.make_image(fill_color=fill_color, back_color=back_color)

        # 尝试使用圆角模块
        try:
            img = qr.make_image(
                image_factory=StyledPilImage,
                module_drawer=RoundedModuleDrawer(),
                fill_color=fill_color,
                back_color=back_color,
            )
        except Exception:
            pass

        # 如果有logo图片，可以叠加（简化版）
        img.save(output_file)
        size = Path(output_file).stat().st_size
        print(f"  ✓ 二维码已生成: {output_file}")
        print(f"  📐 图片尺寸: {img.size[0]}x{img.size[1]}px")
        print(f"  📦 文件大小: {size / 1024:.1f} KB")
        print(f"  📝 数据内容: {data[:80]}{'...' if len(data) > 80 else ''}")
        return True

    except Exception as e:
        print(f"错误：生成二维码失败: {e}")
        return False


def decode(image_file):
    """解析二维码"""
    if not HAS_PYZBAR:
        print("错误：解码需要安装 pyzbar 库")
        print("请执行: pip install pyzbar")
        if sys.platform != "win32":
            print("Linux 还需要: apt-get install libzbar0")
        return False

    try:
        img = Image.open(image_file)
        results = pyzbar_decode(img)

        if not results:
            print(f"未在 {image_file} 中找到二维码")
            return False

        for i, result in enumerate(results):
            print(f"\n二维码 #{i + 1}:")
            print(f"  类型: {result.type}")
            print(f"  数据: {result.data.decode('utf-8', errors='replace')}")
            print(f"  位置: {result.polygon}")

        return True

    except FileNotFoundError:
        print(f"错误：文件 {image_file} 不存在")
        return False
    except Exception as e:
        print(f"错误：解析二维码失败: {e}")
        return False


def batch_encode(input_file, output_dir, fill_color="black", back_color="white"):
    """批量生成二维码 - 从文本文件每行一个数据"""
    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            lines = [line.strip() for line in f if line.strip()]
    except Exception as e:
        print(f"错误：读取文件 {input_file} 失败: {e}")
        return False

    out_path = Path(output_dir)
    out_path.mkdir(parents=True, exist_ok=True)

    print(f"从 {input_file} 读取了 {len(lines)} 条数据")
    success = 0

    for i, line in enumerate(lines):
        try:
            # 使用行号或内容前20字符作为文件名
            safe_name = "".join(c if c.isalnum() or c in '-_' else '_' for c in line[:20])
            if not safe_name:
                safe_name = f"qrcode_{i + 1}"
            out_file = out_path / f"{safe_name}.png"

            qr = qrcode.QRCode(version=None, error_correction=qrcode.constants.ERROR_CORRECT_H, box_size=10, border=4)
            qr.add_data(line)
            qr.make(fit=True)
            img = qr.make_image(fill_color=fill_color, back_color=back_color)
            img.save(out_file)

            print(f"  ✓ #{i + 1} {safe_name[:30]}.png")
            success += 1

        except Exception as e:
            print(f"  ✗ #{i + 1} 生成失败: {e}")

    print(f"\n完成！成功生成 {success}/{len(lines)} 个二维码")
    print(f"输出目录: {out_path}")
    return success > 0


def _show_promotion():
    print("\n" + "=" * 55)
    print("  🔧 qr-code-kit - 二维码生成与解析工具")
    print("  📦 pip install qr-code-kit")
    print("  ☕ 如果帮到了您，欢迎打赏支持:")
    print("     USDT(TRC20): TMPQygMkv42QPeyYnkxMkPwsqs7udbD2Aa")
    print("  ⭐ https://github.com/BoiledSaltedDuck/qr-code-kit")
    print("=" * 55)


def main():
    if len(sys.argv) < 3:
        print("用法:")
        print("  生成二维码:   qr-code encode \"数据内容\" [输出文件]")
        print("  解析二维码:   qr-code decode [二维码图片]")
        print("  批量生成:     qr-code batch [数据文件(每行一条)] [输出目录]")
        print()
        print("示例:")
        print("  qr-code encode \"https://example.com\" myqr.png")
        print("  qr-code decode qrcode.png")
        print("  qr-code batch urls.txt ./qrcodes/")
        sys.exit(1)

    command = sys.argv[1].lower()

    if command == "encode":
        if len(sys.argv) < 3:
            print("用法: qr-code encode \"数据内容\" [输出文件]")
            sys.exit(1)
        data = sys.argv[2]
        output = sys.argv[3] if len(sys.argv) > 3 else "qrcode.png"
        success = encode(data, output)

    elif command == "decode":
        if len(sys.argv) < 3:
            print("用法: qr-code decode [二维码图片]")
            sys.exit(1)
        success = decode(sys.argv[2])

    elif command == "batch":
        if len(sys.argv) < 4:
            print("用法: qr-code batch [数据文件] [输出目录]")
            sys.exit(1)
        success = batch_encode(sys.argv[2], sys.argv[3])

    else:
        print(f"错误：不支持的命令 '{command}'，仅支持 encode/decode/batch")
        sys.exit(1)

    if success:
        _show_promotion()
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
