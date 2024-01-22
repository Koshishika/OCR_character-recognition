# 文字認識（タイヤ）

ocrを用いて、タイヤの文字認識を試みる。
paddleocrを用いた。

# 結果
![output](https://github.com/Koshishika/OCR_character-recognition/assets/80410160/43900267-fcc6-4dea-aba9-2b3aa8ac4ae5)

# 考察
- PaddleOCRが多数の文字を検出し、それらをテキストとして認識されたが、多くのノイズも同時に検出してしまっている。
- 抽出されたテキストは非常に混乱しており、認識された単語の間に関連性が見られない。
- 「BRIDGESTONE」や「DUELER」といった単語が、周囲のノイズによって他の認識されたテキストと混ざってしまった。

# 改善点
- 前処理の改善を行い、画像のコントラストを調整し、文字と背景の区別を明確にする。
- パラメータのチューニングを行う PaddleOCRのパラメータを調整して、誤検出を減らすこと。
- 認識されたテキストに対して後処理を行い、明らかに無関係または不正な単語をフィルタリングする。
- トレーニングデータの改善: 類似したフォントや背景を持つ画像でOCRモデルを再トレーニングして、認識精度を向上させる。
