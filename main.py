"""
丝网花售卖网站 - Streamlit应用主文件
大学生创业项目展示，类似餐厅点单的小程序
"""

import streamlit as st

from products import (
    ALL_PRODUCTS,
    ProductCategory,
    get_products_by_category,
)

# 页面配置
st.set_page_config(
    page_title="丝网花创意工坊",
    page_icon="🌸",
    layout="wide",
    initial_sidebar_state="expanded",
)

# 自定义CSS样式
st.markdown(
    """
<style>
    .main-header {
        text-align: center;
        padding: 1rem;
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
        border-radius: 10px;
        margin-bottom: 2rem;
    }
    .product-card {
        border: 1px solid #e0e0e0;
        border-radius: 10px;
        padding: 1rem;
        margin-bottom: 1rem;
        transition: transform 0.2s;
        background-color: white;
    }
    .product-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 5px 15px rgba(0,0,0,0.1);
    }
    .category-button {
        width: 100%;
        padding: 1rem;
        margin: 0.5rem 0;
        font-size: 1.1rem;
        border-radius: 8px;
    }
    .price-tag {
        color: #e74c3c;
        font-weight: bold;
        font-size: 1.2rem;
    }
    .cart-item {
        padding: 0.5rem;
        border-bottom: 1px solid #eee;
    }
    .stButton > button {
        width: 100%;
    }
</style>
""",
    unsafe_allow_html=True,
)


def init_session_state():
    """初始化session state"""
    if "cart" not in st.session_state:
        st.session_state.cart = {}
    if "current_page" not in st.session_state:
        st.session_state.current_page = "home"
    if "selected_category" not in st.session_state:
        st.session_state.selected_category = ProductCategory.TRADITIONAL


def render_header():
    """渲染页面头部"""
    col1, col2, col3 = st.columns([1, 2, 1])

    with col2:
        st.markdown(
            """
        <div class="main-header">
            <h1>🌸 丝网花创意工坊 🌸</h1>
            <p>大学生创业项目 | 手工制作 | 独特设计 | 支持定制</p>
        </div>
        """,
            unsafe_allow_html=True,
        )

    # 显示购物车信息
    with col3:
        cart_total = sum(item["quantity"] for item in st.session_state.cart.values())
        cart_value = sum(
            item["quantity"] * item["price"] for item in st.session_state.cart.values()
        )

        st.metric("购物车", f"{cart_total} 件商品", f"¥{cart_value:.2f}")

        if st.button("查看购物车", type="primary"):
            st.session_state.current_page = "cart"


def render_home_page():
    """渲染主页"""
    st.markdown("## 🎯 产品分类")

    # 三大类产品导航
    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("### 传统丝网花")
        st.image(
            "images/01-常规产品/基础款-01-单只梅花丝网花.jpg", use_column_width=True
        )
        if st.button("浏览传统丝网花", key="btn_traditional", type="primary"):
            st.session_state.current_page = "category"
            st.session_state.selected_category = ProductCategory.TRADITIONAL
        st.markdown("经典手工制作，传承技艺")

    with col2:
        st.markdown("### 创新丝网花")
        st.image(
            "images/02-创新丝网花/01-婚庆产品-婚礼路引花艺-02.jpg",
            use_column_width=True,
        )
        if st.button("浏览创新丝网花", key="btn_innovative", type="primary"):
            st.session_state.current_page = "category"
            st.session_state.selected_category = ProductCategory.INNOVATIVE
        st.markdown("婚庆商业，创意无限")

    with col3:
        st.markdown("### 新产品")
        st.image("images/03-新产品/01-风铃捕梦网等装饰品-01.png", use_column_width=True)
        if st.button("浏览新产品", key="btn_new", type="primary"):
            st.session_state.current_page = "category"
            st.session_state.selected_category = ProductCategory.NEW
        st.markdown("风铃串珠，多样选择")

    st.markdown("---")

    # 特色产品推荐
    st.markdown("## 🌟 特色推荐")

    # 随机选择4个特色产品
    featured_products = ALL_PRODUCTS[:4]

    cols = st.columns(4)
    for idx, product in enumerate(featured_products):
        with cols[idx]:
            st.image(product.image_path, use_column_width=True)
            st.markdown(f"**{product.name}**")
            st.markdown(
                f'<div class="price-tag">¥{product.price}</div>', unsafe_allow_html=True
            )

            # 添加到购物车按钮
            if st.button("加入购物车", key=f"add_featured_{product.id}"):
                add_to_cart(product.id, product.name, product.price)
                st.success(f"已添加 {product.name} 到购物车!")
                st.rerun()


def render_category_page():
    """渲染分类产品页面"""
    category = st.session_state.selected_category
    products = get_products_by_category(category)

    st.markdown(f"## {category.value}")
    st.markdown(f"共 {len(products)} 个产品")

    # 返回主页按钮
    if st.button("← 返回主页"):
        st.session_state.current_page = "home"
        st.rerun()

    # 产品网格展示
    cols_per_row = 3
    for i in range(0, len(products), cols_per_row):
        cols = st.columns(cols_per_row)

        for j in range(cols_per_row):
            idx = i + j
            if idx < len(products):
                product = products[idx]
                with cols[j]:
                    # 产品卡片
                    st.markdown('<div class="product-card">', unsafe_allow_html=True)

                    # 产品图片
                    try:
                        st.image(product.image_path, use_column_width=True)
                    except Exception:
                        st.image(
                            "https://via.placeholder.com/300x200?text=产品图片",
                            use_column_width=True,
                        )

                    # 产品信息
                    st.markdown(f"### {product.name}")
                    st.markdown(product.description)
                    st.markdown(
                        f'<div class="price-tag">¥{product.price}</div>',
                        unsafe_allow_html=True,
                    )

                    # 数量选择器
                    col_qty1, col_qty2 = st.columns([2, 1])
                    with col_qty1:
                        quantity = st.number_input(
                            "数量",
                            min_value=1,
                            max_value=10,
                            value=1,
                            key=f"qty_{product.id}",
                        )

                    # 添加到购物车按钮
                    with col_qty2:
                        if st.button("加入", key=f"add_{product.id}"):
                            add_to_cart(
                                product.id, product.name, product.price, quantity
                            )
                            st.success(f"已添加 {quantity} 件 {product.name} 到购物车!")
                            st.rerun()

                    st.markdown("</div>", unsafe_allow_html=True)


def render_cart_page():
    """渲染购物车页面"""
    st.markdown("## 🛒 我的购物车")

    cart = st.session_state.cart

    if not cart:
        st.info("购物车是空的，快去挑选喜欢的商品吧！")
        if st.button("返回浏览商品"):
            st.session_state.current_page = "home"
            st.rerun()
        return

    # 购物车商品列表
    total_items = 0
    total_price = 0.0

    for product_id, item in cart.items():
        col1, col2, col3, col4, col5 = st.columns([3, 2, 2, 2, 1])

        with col1:
            st.markdown(f"**{item['name']}**")

        with col2:
            st.markdown(f"单价: ¥{item['price']:.2f}")

        with col3:
            # 数量调整
            new_qty = st.number_input(
                "数量",
                min_value=1,
                max_value=10,
                value=item["quantity"],
                key=f"cart_qty_{product_id}",
            )
            if new_qty != item["quantity"]:
                update_cart_quantity(product_id, new_qty)
                st.rerun()

        with col4:
            item_total = item["price"] * item["quantity"]
            st.markdown(f"小计: ¥{item_total:.2f}")
            total_items += item["quantity"]
            total_price += item_total

        with col5:
            if st.button("❌", key=f"remove_{product_id}"):
                remove_from_cart(product_id)
                st.rerun()

    st.markdown("---")

    # 购物车汇总
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### 总计")
        st.markdown(f"**商品数量:** {total_items} 件")
        st.markdown(f"**商品总价:** ¥{total_price:.2f}")

    with col2:
        st.markdown("### 操作")

        col_btn1, col_btn2 = st.columns(2)
        with col_btn1:
            if st.button("继续购物", use_container_width=True):
                st.session_state.current_page = "home"
                st.rerun()

        with col_btn2:
            if st.button("清空购物车", type="secondary", use_container_width=True):
                clear_cart()
                st.rerun()

    st.markdown("---")

    # 结算按钮
    if st.button("前往结算", type="primary", use_container_width=True):
        st.session_state.current_page = "checkout"
        st.rerun()


def render_checkout_page():
    """渲染结算页面"""
    st.markdown("## 📝 订单结算")

    # 显示购物车摘要
    cart = st.session_state.cart
    if not cart:
        st.warning("购物车为空，无法结算")
        if st.button("返回购物"):
            st.session_state.current_page = "home"
            st.rerun()
        return

    total_price = sum(item["price"] * item["quantity"] for item in cart.values())

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### 订单摘要")
        for product_id, item in cart.items():
            st.markdown(
                f"- {item['name']} × {item['quantity']}: ¥{item['price'] * item['quantity']:.2f}"
            )
        st.markdown(f"**总计: ¥{total_price:.2f}**")

    with col2:
        st.markdown("### 收货信息")

        # 表单
        with st.form("checkout_form"):
            name = st.text_input("收货人姓名", placeholder="请输入姓名")
            phone = st.text_input("联系电话", placeholder="请输入手机号")
            address = st.text_area("收货地址", placeholder="请输入详细地址")
            notes = st.text_area("备注", placeholder="特殊要求或留言")

            # 支付方式
            payment_method = st.radio(
                "支付方式", ["微信支付", "支付宝", "银行卡", "货到付款"]
            )

            submitted = st.form_submit_button("提交订单", type="primary")

            if submitted:
                if not name or not phone or not address:
                    st.error("请填写完整的收货信息")
                else:
                    # 创建订单
                    order_id = create_order(
                        name, phone, address, notes, payment_method, total_price
                    )
                    st.success(f"订单提交成功！订单号: {order_id}")

                    # 清空购物车
                    clear_cart()

                    # 显示订单确认
                    st.markdown("### 订单确认")
                    st.markdown(f"**订单号:** {order_id}")
                    st.markdown(f"**收货人:** {name}")
                    st.markdown(f"**联系电话:** {phone}")
                    st.markdown(f"**收货地址:** {address}")
                    st.markdown(f"**支付方式:** {payment_method}")
                    st.markdown(f"**订单金额:** ¥{total_price:.2f}")

                    if st.button("返回首页"):
                        st.session_state.current_page = "home"
                        st.rerun()


def add_to_cart(product_id: str, name: str, price: float, quantity: int = 1):
    """添加商品到购物车"""
    cart = st.session_state.cart

    if product_id in cart:
        cart[product_id]["quantity"] += quantity
    else:
        cart[product_id] = {"name": name, "price": price, "quantity": quantity}


def update_cart_quantity(product_id: str, quantity: int):
    """更新购物车中商品数量"""
    if product_id in st.session_state.cart:
        if quantity <= 0:
            del st.session_state.cart[product_id]
        else:
            st.session_state.cart[product_id]["quantity"] = quantity


def remove_from_cart(product_id: str):
    """从购物车移除商品"""
    if product_id in st.session_state.cart:
        del st.session_state.cart[product_id]


def clear_cart():
    """清空购物车"""
    st.session_state.cart = {}


def create_order(
    name: str,
    phone: str,
    address: str,
    notes: str,
    payment_method: str,
    total_price: float,
) -> str:
    """创建订单（模拟）"""
    import random
    import time

    # 生成订单号
    order_id = f"ORD{int(time.time())}{random.randint(100, 999)}"

    # 在实际应用中，这里应该将订单保存到数据库
    # 这里只是模拟

    return order_id


def main():
    """主函数"""
    init_session_state()
    render_header()

    # 根据当前页面渲染不同内容
    current_page = st.session_state.current_page

    if current_page == "home":
        render_home_page()
    elif current_page == "category":
        render_category_page()
    elif current_page == "cart":
        render_cart_page()
    elif current_page == "checkout":
        render_checkout_page()

    # 侧边栏 - 购物车预览
    with st.sidebar:
        st.markdown("## 🛍️ 购物车预览")

        cart = st.session_state.cart
        if cart:
            for product_id, item in cart.items():
                st.markdown(f"**{item['name']}** × {item['quantity']}")

            total_items = sum(item["quantity"] for item in cart.values())
            total_price = sum(
                item["price"] * item["quantity"] for item in cart.values()
            )

            st.markdown("---")
            st.markdown(f"**总计:** {total_items} 件商品")
            st.markdown(f"**金额:** ¥{total_price:.2f}")

            if st.button("去结算", type="primary", use_container_width=True):
                st.session_state.current_page = "checkout"
                st.rerun()
        else:
            st.info("购物车为空")

        st.markdown("---")
        st.markdown("## ℹ️ 关于我们")
        st.markdown("""
        大学生创业项目  
        手工丝网花制作  
        支持定制设计  
        联系电话: 138-XXXX-XXXX  
        微信: silkflower_shop
        """)

        # 页面导航
        st.markdown("---")
        st.markdown("## 📱 页面导航")

        if st.button("🏠 首页", use_container_width=True):
            st.session_state.current_page = "home"
            st.rerun()

        if st.button("🛒 购物车", use_container_width=True):
            st.session_state.current_page = "cart"
            st.rerun()


if __name__ == "__main__":
    main()
