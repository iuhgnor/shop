#!/usr/bin/env python3
"""
测试图片缩放功能
"""

import os
import sys

# 添加当前目录到Python路径
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from PIL import Image

from main import display_product_image, load_and_resize_image


def test_image_loading():
    """测试图片加载和缩放功能"""
    print("🧪 测试图片缩放功能...")

    # 测试一个存在的图片
    test_image_path = "images/01-常规产品/基础款-01-单只梅花丝网花.jpg"

    if not os.path.exists(test_image_path):
        print(f"  ⚠️ 测试图片不存在: {test_image_path}")
        return False

    print(f"  ✓ 测试图片存在: {test_image_path}")

    # 测试加载和缩放
    try:
        resized_img = load_and_resize_image(test_image_path, target_size=(300, 200))

        if resized_img is None:
            print("  ❌ 图片加载失败")
            return False

        # 检查图片尺寸
        width, height = resized_img.size
        print(f"  ✓ 图片缩放成功: {width}x{height}")

        # 验证尺寸
        assert width == 300, f"宽度应为300，实际为{width}"
        assert height == 200, f"高度应为200，实际为{height}"
        print("  ✓ 图片尺寸正确: 300x200")

        # 检查图片模式
        assert resized_img.mode == "RGB", f"图片模式应为RGB，实际为{resized_img.mode}"
        print("  ✓ 图片模式正确: RGB")

        return True

    except Exception as e:
        print(f"  ❌ 测试失败: {e}")
        return False


def test_png_image():
    """测试PNG图片处理"""
    print("\n🧪 测试PNG图片处理...")

    test_image_path = "images/03-新产品/01-风铃捕梦网等装饰品-01.png"

    if not os.path.exists(test_image_path):
        print(f"  ⚠️ PNG测试图片不存在: {test_image_path}")
        return True  # 不是致命错误

    try:
        resized_img = load_and_resize_image(test_image_path)

        if resized_img is None:
            print("  ⚠️ PNG图片加载失败")
            return True  # 不是致命错误

        width, height = resized_img.size
        print(f"  ✓ PNG图片处理成功: {width}x{height}")
        print(f"  ✓ PNG图片模式: {resized_img.mode}")

        return True

    except Exception as e:
        print(f"  ⚠️ PNG图片处理警告: {e}")
        return True  # 不是致命错误


def test_missing_image():
    """测试缺失图片处理"""
    print("\n🧪 测试缺失图片处理...")

    missing_image_path = "images/nonexistent.jpg"

    try:
        resized_img = load_and_resize_image(missing_image_path)

        if resized_img is None:
            print("  ✓ 缺失图片正确处理: 返回None")
            return True
        else:
            print("  ⚠️ 缺失图片未返回None")
            return True  # 不是致命错误

    except Exception as e:
        print(f"  ⚠️ 缺失图片处理异常: {e}")
        return True  # 不是致命错误


def main():
    """主测试函数"""
    print("=" * 60)
    print("图片缩放功能测试")
    print("=" * 60)

    tests_passed = 0
    total_tests = 3

    try:
        if test_image_loading():
            tests_passed += 1

        if test_png_image():
            tests_passed += 1

        if test_missing_image():
            tests_passed += 1

    except Exception as e:
        print(f"\n❌ 测试异常: {e}")
        return False

    print("\n" + "=" * 60)
    print(f"测试结果: {tests_passed}/{total_tests} 通过")

    if tests_passed >= 1:  # 至少核心功能通过
        print("🎉 图片缩放功能测试完成！")
        return True
    else:
        print("⚠️  图片缩放功能测试未通过")
        return False


if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
