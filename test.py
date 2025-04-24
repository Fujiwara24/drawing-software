import cv2
import numpy as np

# --- グローバル変数 ---
drawing = False  # マウスボタンが押されているかどうかのフラグ
marker_type = cv2.MARKER_CROSS  # 初期のマーカータイプ
drawing_img = None  # 描画対象の画像 (読み込み後に設定)
window_name = 'oekaki' # ウィンドウ名
marker_color = (0, 0, 255)  # マーカーの色 (BGR形式で赤)
marker_size = 20         # マーカーのサイズ
marker_thickness = 2     # マーカーの太さ

# --- マウスイベントのコールバック関数 ---
def draw_marker(event, x, y, flags, param):
    global drawing, marker_type, drawing_img

    # 左ボタンが押された時
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        # 現在の位置にマーカーを描画
        cv2.drawMarker(drawing_img, (x, y), marker_color, marker_type, marker_size, marker_thickness)

    # マウスが移動した時
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing:
            # 現在の位置にマーカーを描画
            cv2.drawMarker(drawing_img, (x, y), marker_color, marker_type, marker_size, marker_thickness)

    # 左ボタンが離された時
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        # 離された位置にもマーカーを描画（クリック時にも描画されるように）
        cv2.drawMarker(drawing_img, (x, y), marker_color, marker_type, marker_size, marker_thickness)



# --- メイン処理 ---
def main():
    global marker_type, drawing_img # グローバル変数をmain関数内で使う宣言

    # 画像をロード
    image_path = 'AIT_formula.jpg'
    img = cv2.imread(image_path)

    # 読み込んだ画像のコピーに対して描画を行う
    drawing_img = img.copy()

    # ウィンドウを作成し、マウスコールバック関数を設定
    cv2.namedWindow(window_name)

    cv2.waitKey(3)  # ウィンドウが初期化されるのを待つ
    cv2.imshow(window_name, drawing_img)


    cv2.setMouseCallback(window_name, draw_marker)
    cv2.imshow(window_name, drawing_img)

    print("\n--- 操作方法 ---")
    print("マウス左ボタンを押しながらドラッグ: 描画")
    print("スペースキー: マーカーの種類を切り替え (CROSS <-> TILTED_CROSS)")
    print("S キー: 現在の画像を 'draw.png' として保存")
    print("ESC キー: アプリケーションを終了")
    print("---------------")

    # メインループ
    while True:
        # 現在の描画状態の画像を表示
        cv2.imshow(window_name, drawing_img)

        # キー入力を待つ (20ms)
        key = cv2.waitKey(20) & 0xFF

        # ESCキーが押されたらループを抜ける
        if key == 27:
            print("ESCキーが押されました。アプリケーションを終了します。")
            break

        # スペースキーが押されたらマーカータイプを切り替える
        elif key == ord(' '):
            if marker_type == cv2.MARKER_CROSS:
                marker_type = cv2.MARKER_TILTED_CROSS
                print("マーカータイプを TILTED_CROSS に変更しました。")
            else:
                marker_type = cv2.MARKER_CROSS
                print("マーカータイプを CROSS に変更しました。")

        # 's' キーが押されたら画像を保存する
        elif key == ord('s'):
            save_path = 'draw.png'
            cv2.imwrite(save_path, drawing_img)
            print(f"現在の画像を '{save_path}' として保存しました。")

    # アプリケーション終了時にウィンドウを閉じる
    cv2.destroyAllWindows()


# スクリプトとして実行された場合にmain関数を呼び出す
if __name__ == '__main__':
    main()