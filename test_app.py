#!/usr/bin/env python3
"""
丝网花售卖网站 - 应用测试脚本
验证核心功能是否正常工作
"""

import os
import sys

# 添加当前目录到Python路径
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from products import (
    ALL_PRODUCTS,
    ProductCategory,
    get_product_by_id,
    get_products_by_category,
)


def test_product_data():
    """测试产品数据"""
    print("🧪 测试产品数据...")

    # 测试总产品数量
    assert len(ALL_PRODUCTS) == 25, f"预期25个产品，实际{len(ALL_PRODUCTS)}个"
    print(f"  ✓ 总产品数量: {len(ALL_PRODUCTS)}")

    # 测试分类产品数量
    trad_count = len(get_products_by_category(ProductCategory.TRADITIONAL))
    innov_count = len(get_products_by_category(ProductCategory.INNOVATIVE))
    new_count = len(get_products_by_category(ProductCategory.NEW))

    assert trad_count == 6, f"传统丝网花应有6个，实际{trad_count}个"
    assert innov_count == 11, f"创新丝网花应有11个，实际{innov_count}个"
    assert new_count == 8, f"新产品应有8个，实际{new_count}个"

    print(f"  ✓ 传统丝网花: {trad_count} 个")
    print(f"  ✓ 创新丝网花: {innov_count} 个")
    print(f"  ✓ 新产品: {new_count} 个")

    # 测试产品属性
    sample_product = ALL_PRODUCTS[0]
    assert hasattr(sample_product, "id"), "产品缺少id属性"
    assert hasattr(sample_product, "name"), "产品缺少name属性"
    assert hasattr(sample_product, "price"), "产品缺少price属性"
    assert hasattr(sample_product, "category"), "产品缺少category属性"
    assert hasattr(sample_product, "image_path"), "产品缺少image_path属性"

    print("  ✓ 产品数据结构正确")

    # 测试图片文件是否存在（至少检查一个）
    import os

    if os.path.exists(sample_product.image_path):
        print(f"  ✓ 图片文件存在: {sample_product.image_path}")
    else:
        print(f"  ⚠️ 图片文件不存在: {sample_product.image_path}（可能路径问题）")

    return True


def test_product_lookup():
    """测试产品查找功能"""
    print("\n🧪 测试产品查找功能...")

    # 测试按ID查找
    test_id = "trad-001"
    product = get_product_by_id(test_id)
    assert product is not None, f"找不到ID为{test_id}的产品"
    assert product.id == test_id, f"产品ID不匹配"
    print(f"  ✓ 按ID查找产品: {product.name}")

    # 测试按分类查找
    trad_products = get_products_by_category(ProductCategory.TRADITIONAL)
    assert len(trad_products) > 0, "按分类查找返回空列表"
    print(
        f"  ✓ 按分类查找: {ProductCategory.TRADITIONAL.value} - {len(trad_products)}个产品"
    )

    return True


def test_price_ranges():
    """测试价格范围"""
    print("\n🧪 测试价格范围...")

    prices = [p.price for p in ALL_PRODUCTS]
    min_price = min(prices)
    max_price = max(prices)

    print(f"  ✓ 最低价格: ¥{min_price}")
    print(f"  ✓ 最高价格: ¥{max_price}")
    print(f"  ✓ 价格范围: ¥{min_price} - ¥{max_price}")

    # 验证价格合理性
    assert min_price > 0, "价格必须大于0"
    assert max_price < 1000, "价格过高，请检查"

    return True


def test_image_paths():
    """测试图片路径"""
    print("\n🧪 测试图片路径...")

    valid_extensions = {".jpg", ".jpeg", ".png", ".gif"}
    invalid_paths = []

    for product in ALL_PRODUCTS[:5]:  # 只检查前5个
        path = product.image_path
        ext = os.path.splitext(path)[1].lower()

        if ext not in valid_extensions:
            invalid_paths.append((product.id, path))
        else:
            print(f"  ✓ {product.id}: 图片格式正确 ({ext})")

    if invalid_paths:
        print(f"  ⚠️ 发现{len(invalid_paths)}个可能无效的图片路径")
        for pid, path in invalid_paths:
            print(f"    - {pid}: {path}")

    return True


def main():
    """主测试函数"""
    print("=" * 60)
    print("丝网花售卖网站 - 应用测试")
    print("=" * 60)

    tests_passed = 0
    total_tests = 4

    try:
        if test_product_data():
            tests_passed += 1

        if test_product_lookup():
            tests_passed += 1

        if test_price_ranges():
            tests_passed += 1

        if test_image_paths():
            tests_passed += 1

    except AssertionError as e:
        print(f"\n❌ 测试失败: {e}")
        return False
    except Exception as e:
        print(f"\n❌ 测试异常: {e}")
        return False

    print("\n" + "=" * 60)
    print(f"测试结果: {tests_passed}/{total_tests} 通过")

    if tests_passed == total_tests:
        print("🎉 所有测试通过！应用准备就绪。")
        return True
    else:
        print("⚠️  部分测试未通过，请检查问题。")
        return False


if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
