"""
商品库存管理系统 - Web版本
基于Flask框架
"""

from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
import json
import os

app = Flask(__name__)
app.secret_key = 'your-secret-key-here'  # 用于会话安全

# 数据文件路径
DATA_FILE = "products.json"

def load_data():
    """从文件加载数据"""
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}

def save_data(data):
    """保存数据到文件"""
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

# 全局商品数据
products = load_data()

@app.route('/')
def index():
    """首页 - 显示所有商品"""
    return render_template('index.html', products=products)

@app.route('/add', methods=['GET', 'POST'])
def add_product():
    """添加商品"""
    global products
    
    if request.method == 'POST':
        name = request.form['name'].strip()
        quantity = request.form['quantity']
        price = request.form['price']
        
        if not name:
            flash('商品名称不能为空', 'error')
            return redirect(url_for('add_product'))
        
        try:
            quantity = int(quantity)
            price = float(price)
            
            if quantity < 0 or price < 0:
                flash('商品数量和价格必须大于等于0', 'error')
                return redirect(url_for('add_product'))
            
            if name in products:
                flash(f'商品 {name} 已存在', 'warning')
                return redirect(url_for('index'))
            
            products[name] = {"quantity": quantity, "price": price}
            save_data(products)
            flash(f'商品 {name} 添加成功', 'success')
            return redirect(url_for('index'))
            
        except ValueError:
            flash('请输入有效的数量和价格', 'error')
            return redirect(url_for('add_product'))
    
    return render_template('add.html')

@app.route('/delete/<name>')
def delete_product(name):
    """删除商品"""
    global products
    
    if name in products:
        del products[name]
        save_data(products)
        flash(f'商品 {name} 删除成功', 'success')
    else:
        flash(f'未找到商品 {name}', 'error')
    
    return redirect(url_for('index'))

@app.route('/edit/<name>', methods=['GET', 'POST'])
def edit_product(name):
    """编辑商品"""
    global products
    
    if name not in products:
        flash(f'未找到商品 {name}', 'error')
        return redirect(url_for('index'))
    
    if request.method == 'POST':
        quantity = request.form['quantity']
        price = request.form['price']
        
        try:
            if quantity:
                quantity = int(quantity)
                if quantity < 0:
                    flash('数量不能为负数', 'error')
                    return redirect(url_for('edit_product', name=name))
                products[name]['quantity'] = quantity
            
            if price:
                price = float(price)
                if price < 0:
                    flash('价格不能为负数', 'error')
                    return redirect(url_for('edit_product', name=name))
                products[name]['price'] = price
            
            save_data(products)
            flash(f'商品 {name} 更新成功', 'success')
            return redirect(url_for('index'))
            
        except ValueError:
            flash('请输入有效的数值', 'error')
            return redirect(url_for('edit_product', name=name))
    
    product = products[name]
    return render_template('edit.html', name=name, product=product)

@app.route('/search')
def search_product():
    """搜索商品"""
    query = request.args.get('q', '').strip()
    
    if not query:
        return redirect(url_for('index'))
    
    # 搜索匹配的商品
    search_results = {}
    for name, info in products.items():
        if query.lower() in name.lower():
            search_results[name] = info
    
    return render_template('search.html', query=query, results=search_results)

@app.route('/statistics')
def statistics():
    """库存统计"""
    if not products:
        flash('暂无商品信息', 'info')
        return redirect(url_for('index'))
    
    total_products = len(products)
    total_quantity = sum(info['quantity'] for info in products.values())
    total_value = sum(info['quantity'] * info['price'] for info in products.values())
    
    # 找出库存最多的商品
    max_stock = max(products.items(), key=lambda x: x[1]['quantity'])
    # 找出库存最少的商品
    min_stock = min(products.items(), key=lambda x: x[1]['quantity'])
    # 找出价值最高的商品
    max_value_item = max(products.items(), key=lambda x: x[1]['quantity'] * x[1]['price'])
    
    return render_template('statistics.html', 
                          total_products=total_products,
                          total_quantity=total_quantity,
                          total_value=total_value,
                          max_stock=max_stock,
                          min_stock=min_stock,
                          max_value_item=max_value_item)

@app.route('/api/products')
def api_products():
    """API接口：获取所有商品"""
    return jsonify(products)

@app.route('/api/product/<name>')
def api_product(name):
    """API接口：获取单个商品"""
    if name in products:
        return jsonify({"name": name, "info": products[name]})
    else:
        return jsonify({"error": "商品不存在"}), 404

if __name__ == '__main__':
    # 创建templates目录（如果不存在）
    os.makedirs('templates', exist_ok=True)

    print("服务器启动...")
    print("访问: http://localhost:8000")
    print("服务器启动完成")
    print("等待连接...")
    print("服务器已启动，等待连接...")

    
    # 运行Flask应用
    app.run(debug=True, host='0.0.0.0', port=8000, threaded=True, use_reloader=False)