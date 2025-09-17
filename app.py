import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="BlockPedia",
    page_icon="📑",
    layout="wide"
)

with st.sidebar:
    st.sidebar.image(
        "https://i.imgur.com/pwYe3ox.png",
        use_container_width=True
    )
    st.sidebar.markdown("📘 **About**")
    st.sidebar.markdown("""
    Blockpedia adalah knowledge base terbuka tentang dunia Web3 — meliputi blockchain, smart contracts, crypto, DAOs, DeFi, NFTs, metaverse, dan seterusnya.

    Di sini, kamu bisa menemukan:
    
    - 📚 Concepts & Definitions → istilah Web3 yang jelas dan terstruktur.
    
    - 🛡 Best Practices → keamanan smart contract, optimasi gas, governance patterns.
    
    - 🗂 Taxonomy → klasifikasi Web3 (protocols, infra, dApps, metaverse).
    
    - 📝 Documentation & Case Studies → referensi, proyek nyata, standar teknis (ERCs, BIPs, dsb).

    Blockpedia terhubung dengan Learn3, STC DataHub, dan RANTAI Nexus, menjadikannya bagian dari ekosistem belajar, praktik, dan kolaborasi Web3.

    ---
    #### 🔮 Vision Statement

    > “Blockpedia: The Open Brain of Web3.”
    
    Kami percaya bahwa pengetahuan Web3 harus:
    
    - Terbuka → semua orang bisa mengakses dan berkontribusi.
    
    - Terstruktur → mudah dipahami, dihubungkan, dan diperbarui.
    
    - Hidup → selalu berevolusi seiring eksperimen, penelitian, dan inovasi baru.
    
    Blockpedia adalah tempat di mana pengetahuan bertemu praktik, lalu kembali memperkaya komunitas.
    
    ---
    ### ❓ How to Log in
    
    Blockpedia menggunakan Sign-In with Ethereum (SIWE) sebagai mekanisme login.

    - Saat login, hanya wallet address kamu yang tercatat.
    
    - Tidak ada data lain yang disimpan tanpa izinmu.
    
    - Jika ingin, kamu bisa menambahkan nama tampilan (display name) untuk memudahkan interaksi komunitas.
    
    - Kamu tetap bisa menjelajah Blockpedia tanpa login, tapi dengan login kamu bisa:
    
      - 🖊️ Berkontribusi langsung (edit / tambah artikel).
    
      - 🗳️ Ikut voting komunitas untuk konten prioritas.
    
      - 📌 Menyimpan bookmark atau koleksi pribadi.
    
    ---
    ### 🧩 RANTAI Ecosystem
    1. [STC Analytics](https://stc-analytics.streamlit.app/)
    2. [STC GasVision](https://stc-gasvision.streamlit.app/)
    3. [STC Converter](https://stc-converter.streamlit.app/)
    4. [STC Bench](https://stc-bench.streamlit.app/)
    5. [STC Insight](https://stc-insight.streamlit.app/)
    6. [STC Plugin](https://smartourism.elpeef.com/)
    7. [SmartFaith](https://smartfaith.streamlit.app/)
    8. [Learn3](https://learn3.streamlit.app/)
    9. [Nexus](https://rantai-nexus.streamlit.app/)
    10. [DataHub](https://stc-data.streamlit.app/)
    11. [STC GasX](https://stc-gasx.streamlit.app/)

    ---
    #### 🙌 Dukungan & kontributor
    - ⭐ **Star / Fork**: [GitHub repo](https://github.com/mrbrightsides/blockpedia)
    - Built with 💙 by [Khudri](https://s.id/khudri)
    - Dukung pengembangan proyek ini melalui: 
      [💖 GitHub Sponsors](https://github.com/sponsors/mrbrightsides) • 
      [☕ Ko-fi](https://ko-fi.com/khudri) • 
      [💵 PayPal](https://www.paypal.com/paypalme/akhmadkhudri) • 
      [🍵 Trakteer](https://trakteer.id/akhmad_khudri)

    Versi UI: v1.0 • Streamlit • Theme Dark
    """)

def embed_iframe(src, hide_top_px=72, height=800):
    components.html(f"""
    <div style="height:{height}px; overflow:hidden; position:relative;">
        <iframe src="{src}" 
                style="width:100%; height:{height + hide_top_px}px; border:none; position:relative; top:-{hide_top_px}px;">
        </iframe>
    </div>
    """, height=height)

# URL Ohara
iframe_url = "https://ohara.ai/mini-apps/9ae7b454-a3e4-47ba-ae7e-22b021377545"

# Panggil fungsi
embed_iframe(iframe_url, hide_top_px=110, height=800)
