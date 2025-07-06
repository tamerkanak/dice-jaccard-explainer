import streamlit as st
from typing import Set

def dice_coefficient(set1: set, set2: set) -> float:
    if not set1 and not set2:
        return 1.0
    return 2 * len(set1 & set2) / (len(set1) + len(set2))

def jaccard_index(set1: set, set2: set) -> float:
    if not set1 and not set2:
        return 1.0
    return len(set1 & set2) / len(set1 | set2)

def text_to_set(text: str) -> set:
    return set(word.strip().lower() for word in text.split() if word.strip())

st.title("🎲 Dice & Jaccard: Benzerlikte Şampiyonlar Ligi!")

st.markdown("""
### 🤔 Neden Benzerlik Ölçeriz?
- 🤖 Makine öğrenmesinde benzerlik, verinin ruhunu yakalamak için şart! Modelin başarısı için olmazsa olmaz.
- 🔍 Arama, öneri, kümeleme, veri temizliği... Kısacası, verinin olduğu her yerde benzerlik var!
- 📊 Dice ve Jaccard, benzerlik ölçümünde adeta Messi & Ronaldo gibi: Herkesin favorisi, herkesin dilinde!
""")

st.markdown("---")

st.markdown("### ⭐️ Dice & Jaccard Neden Bu Kadar Önemli?")
st.markdown("""
- 🟢 Küme tabanlı oldukları için metin, etiket, ilgi alanı, ürün kategorisi... Ne verirsen ver, hemen anlarlar!
- ⚡️ Hesaplaması jet hızıyla, yoruma kapalı: 0-1 arası net skor, kafa karışıklığı yok!
- 🧠 Makine öğrenmesinde öznitelik mühendisliği, kümeleme, veri temizliği ve öneri sistemlerinde tam bir joker.
- 🔄 Küçük değişikliklere bile hassas, sonuçları hemen gösterir.
- 🌍 Metin madenciliği, biyoinformatik, bilgi erişimi... Her yerde, her zaman, herkesin elinin altında!
""")

st.markdown("---")

st.markdown("### 📏 Tanımlar ve Formüller (Korkma, Çok Kolay!)")

# Dice Coefficient
st.markdown("**Dice Coefficient:** (Ortakları ikiyle çarp, toplam elemana böl!)")
col_dice_img, col_dice_formula = st.columns([1, 1])
with col_dice_img:
    st.image("Dice.png", width=300)
with col_dice_formula:
    st.markdown("<div style='margin-top: 60px'></div>", unsafe_allow_html=True)
    st.latex(r"Dice(A, B) = \frac{2 |A \cap B|}{|A| + |B|}")

# Jaccard Index
st.markdown("**Jaccard Index:** (Ortakları, birleşime böl!)")
col_jaccard_img, col_jaccard_formula = st.columns([1, 1])
with col_jaccard_img:
    st.image("jaccard.png", width=300)
with col_jaccard_formula:
    st.markdown("<div style='margin-top: 60px'></div>", unsafe_allow_html=True)
    st.latex(r"Jaccard(A, B) = \frac{|A \cap B|}{|A \cup B|}")

st.markdown("0: Hiç benzerlik yok, 1: Tam benzerlik! (Yani 1 = ruh ikizi)")

st.markdown("---")

st.markdown("### 🚦 Hızlı Örnekler (Gerçek Hayattan!)")
st.markdown("**1. Tamamen Aynı Küme** 🟢\nA = {spor, futbol, transfer} | B = {spor, futbol, transfer}  ")
st.latex(r"Dice = \frac{2 \times 3}{3+3} = 1")
st.latex(r"Jaccard = \frac{3}{3} = 1")
st.markdown("**2. Hiç Ortak Eleman Yok** 🔴\nA = {yapay zeka, makine öğrenmesi} | B = {finans, ekonomi}  ")
st.latex(r"Dice = \frac{2 \times 0}{2+2} = 0")
st.latex(r"Jaccard = \frac{0}{4} = 0")
st.markdown("**3. Kısmi Benzerlik** 🟡\nA = {elektronik, bilgisayar, aksesuar} | B = {bilgisayar, aksesuar, telefon}  ")
st.markdown("Ortak: {bilgisayar, aksesuar}")
st.latex(r"Dice = \frac{2 \times 2}{3+3} = 0.667")
st.latex(r"Jaccard = \frac{2}{4} = 0.5")

st.markdown("---")

with st.expander("🎁 Sürpriz Not: Jaccard Index'in Gizli Kimliği!"):
    st.markdown("""
    Evet, doğru duydun! Jaccard Index'in bir diğer adı da **Intersection over Union (IoU)** ve bu isimle özellikle **görüntü işleme** dünyasında meşhur. 
    
    📸 **Nerede kullanılıyor?**
    - Özellikle **nesne tespiti (object detection)** algoritmalarında, modelin bulduğu kutu ile gerçek kutunun ne kadar çakıştığını ölçmek için kullanılır.
    - Mesela bir yapay zeka, bir fotoğrafta kediyi bulduysa, tahmin ettiği kutu ile gerçek kutunun kesişimi/birleşimi oranı tam olarak IoU yani Jaccard Index!
    
    > "Bir gün Jaccard Index'in IoU olarak karşına çıkarsa şaşırma, o hâlâ eski dostun!"
    """)
    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        st.image("iou_example.png", caption="IoU (Intersection over Union) - Görüntü İşlemede Jaccard Index'in Kullanımı", width=400)


st.header("📝 Kendi Kümenizi Girin ve Hesaplayın!")
col1, col2 = st.columns(2)
with col1:
    text1 = st.text_area("1. Metin veya etiket listesi", "spor futbol transfer")
with col2:
    text2 = st.text_area("2. Metin veya etiket listesi", "futbol basketbol ekonomi")

set1 = text_to_set(text1)
set2 = text_to_set(text2)

st.write(f"**1. Küme:** {set1}")
st.write(f"**2. Küme:** {set2}")

if set1 or set2:
    dice = dice_coefficient(set1, set2)
    jaccard = jaccard_index(set1, set2)
    st.success(f"🎲 Dice Coefficient: {dice:.3f} — (Ne kadar ortak var?)")
    st.info(f"🟩 Jaccard Index: {jaccard:.3f} — (Gerçekten ne kadar benzer?)")
    st.markdown(f"- 🤝 **Ortak elemanlar:** {set1 & set2}")
    st.markdown(f"- 🧮 **Birleşim:** {set1 | set2}")
    st.latex(rf"Dice = \frac{{2 \times {len(set1 & set2)}}}{{{len(set1)} + {len(set2)}}}")
    st.latex(rf"Jaccard = \frac{{{len(set1 & set2)}}}{{{len(set1 | set2)}}}")
else:
    st.warning("Biraz veri gir, eğlence başlasın!")

st.markdown("---")

st.markdown("### 🧠 Benzerlik Eşiğiyle Otomatik Sınıflandırma (Yapay Zeka Gibi Düşün!)")
st.markdown("İki küme gir, bir eşik seç, bakalım Dice/Jaccard'a göre 'Benzer' mi 'Farklı' mı? Gerçek hayatta veri birleştirme, otomatik etiketleme gibi işlerde tam bir kurtarıcı!")

col_a, col_b = st.columns(2)
with col_a:
    thresh_a = st.text_input("A kümesi", "kanser diyabet hipertansiyon")
with col_b:
    thresh_b = st.text_input("B kümesi", "diyabet obezite kalp hastalığı")

thresh_set_a = text_to_set(thresh_a)
thresh_set_b = text_to_set(thresh_b)
thresh = st.slider("Benzerlik eşiği (%)", min_value=0, max_value=100, value=50, step=1)
metric = st.radio("Hangi metrikle?", ["Dice", "Jaccard"], horizontal=True)

if metric == "Dice":
    sim_score = dice_coefficient(thresh_set_a, thresh_set_b)
else:
    sim_score = jaccard_index(thresh_set_a, thresh_set_b)

st.write(f"{metric} skoru: {sim_score:.3f}")
if sim_score >= thresh/100:
    st.success("✅ Benzer! (Aynı takımdasınız!)")
else:
    st.error("❌ Farklı! (Henüz ortak yönünüz az)")

st.markdown("---")

st.markdown("### 🧩 Benzerlik Skorunu Öznitelik Olarak Kullan! (Modeline Güç Kat!)")
st.markdown("Makine öğrenmesinde, iki metin/etiket arasındaki benzerlik skoru, modelinize eklenebilecek gizli bir süper güç! Aşağıda örnek bir tablo görebilirsin:")

col3, col4 = st.columns(2)
with col3:
    feat1 = st.text_input("A kümesi (ör: kullanıcı ilgi alanları)", "yapay zeka makine öğrenmesi veri bilimi")
with col4:
    feat2 = st.text_input("B kümesi (ör: kurs etiketleri)", "makine öğrenmesi derin öğrenme yapay zeka")

feat_set1 = text_to_set(feat1)
feat_set2 = text_to_set(feat2)
feat_dice = round(dice_coefficient(feat_set1, feat_set2), 3)
feat_jaccard = round(jaccard_index(feat_set1, feat_set2), 3)

import pandas as pd
feature_df = pd.DataFrame([
    {"A Kümesi": feat1, "B Kümesi": feat2, "Dice": feat_dice, "Jaccard": feat_jaccard}
])
st.dataframe(feature_df)
st.markdown("Bu skorlar, modeline eklenince iki nesne/metin/etiket arasındaki benzerliği sayısal olarak gösterebilir, modelini bir üst seviyeye çıkarabilirsin!")

st.markdown("---")

st.markdown("### 💡 Nerelerde Kullanılır? (Şöyle Söyleyeyim Kullanım Durumu Bayağı Yoğun :D)")
st.markdown("""
- 🤖 Makine öğrenmesi: Kümeleme, öznitelik mühendisliği, veri temizliği, öneri sistemleri... (Yani ML'nin kalbi!)
- 📝 Metin madenciliği: Benzer doküman bulma, etiket eşleştirme, spam tespiti...
- 🧬 Biyoinformatik: DNA/protein dizisi karşılaştırma, hastalık benzerliği...
""")

st.markdown("---")

st.markdown("### 📚 Daha Fazla Bilgi")
st.markdown("- [Wikipedia: Sørensen–Dice coefficient](https://en.wikipedia.org/wiki/S%C3%B8rensen%E2%80%93Dice_coefficient)")
st.markdown("- [Wikipedia: Jaccard index](https://en.wikipedia.org/wiki/Jaccard_index)") 
