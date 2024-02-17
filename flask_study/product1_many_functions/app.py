"""
たぬハック, Flaskのrender_templateでHTML・CSS・JavaScriptファイルを読み込む, 
https://tanuhack.com/flask-jinja2-import/, 2023/12/21


twilo BLOG, コミュニケーションの未来を築く, Flaskアプリケーションの実行方法
https://www.twilio.com/ja/blog/how-to-run-a-flask-application-jp, 2023/12/21


Hatena Blog, 学んだことをメモするブログ, Flaskを使って画像データをアップロードする方法
https://progmemo.hatenablog.jp/entry/2022/07/19/020830, 2023/12/21

起動方法
app.pyがあるdir内で「flask run」をして実行
"""


from flask import Flask, render_template, request, url_for, redirect
import os

# ==================================================
# インスタンス生成
# ==================================================
app = Flask(__name__)
# ==================================================
# ルーティング
# ==================================================


@app.route('/')
def index():
	return render_template('index.html')

# ルーティングの設定
# http://---//item-listを実行した場合に,<h1>商品一覧ページです</h1>を表示させる.
# 1.@app.route()の引数に適切な値を設定する
# 2.returnに適切な値を設定する
@app.route('/item-list')
def itemlist():
    return "<h1>商品一覧ページです</h1>"

# http://---//item-list2/idを実行した場合に<h1>id = ??です</h1>をhtml形式で表示させる.
# このときのidの値は,渡した値に10を足した値を表示させるものとする.(id=10を渡したならば「id=20です」と表示させる)
# 1.@app.route()の引数に適切な値を設定する
# 2.itemlist2()の引数に適切な値を設定する
# 3.returnに適切な値を設定する
@app.route('/item-list2/<int:id>')
def itemlist2(id):
    id += 10
    return f"<h1>id = {id}です</h1>"


"""
画像ファイルのアップロード
"""
@app.route('/upload', methods=['GET', 'POST'])
def upload():
    # URLでhttp://127.0.0.1:5000/uploadを指定したときはGETリクエストとなるのでこっち
    if request.method == 'GET':
        return render_template('upload.html')
    # formでsubmitボタンが押されるとPOSTリクエストとなるのでこっち
    elif request.method == 'POST':
        file = request.files['example']
        file.save(os.path.join('./static/image', file.filename))
        return redirect(url_for('uploaded_file', filename=file.filename))


@app.route('/uploaded_file/<string:filename>')
def uploaded_file(filename):
    return render_template('uploaded_file.html', filename=filename)


@app.route('/add_input')
def add_input():
    return render_template('add_input.html')


# ==================================================
# 実行
# ==================================================
if __name__ == '__main__':
    app.run()