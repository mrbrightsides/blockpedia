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
    ### 🧩 STC Ecosystem
    1. [STC Analytics](https://stc-analytics.streamlit.app/)
    2. [STC GasVision](https://stc-gasvision.streamlit.app/)
    3. [STC Converter](https://stc-converter.streamlit.app/)
    4. [STC Bench](https://stc-bench.streamlit.app/)
    5. [STC Insight](https://stc-insight.streamlit.app/)
    6. [STC Plugin](https://smartourism.elpeef.com/)
    7. [STC GasX](https://stc-gasx.streamlit.app/)
    8. [STC CarbonPrint](https://stc-carbonprint.streamlit.app/)
    9. [STC ImpactViz](https://stc-impactviz.streamlit.app/)
    10. [DataHub](https://stc-data.streamlit.app/)

    ---
    ### ⛓ RANTAI Communities

    > 💡 RANTAI Communities adalah ekosistem apps eksperimental berbasis Web3 & AI untuk riset, kolaborasi, dan inovasi. Dibangun di atas 3 core: Dev → Build, Net → Connect, Lab → Grow.
    
    🔧 Dev → “Build the chain”
    1. [Numerical Methods Lab](https://metnumlab.streamlit.app/)
    2. [Computational Analytics Studio](https://komnumlab.streamlit.app/)
    3. [BlockPedia](https://blockpedia.streamlit.app/)
    4. [Learn3](https://learn3.streamlit.app/)
    5. [LearnPy](https://rantai-learnpy.streamlit.app/)
    6. [Cruise](https://rantai-cruise.streamlit.app/)
    7. [IndustriX](https://rantai-industrix.streamlit.app/)

    🌐 Net → “Connect the chain”
    1. [SmartFaith](https://smartfaith.streamlit.app/)
    2. [Nexus](https://rantai-nexus.streamlit.app/)
    3. [Decentralized Supply Chain](https://rantai-trace.streamlit.app/)
    4. [ESG Compliance Manager](https://rantai-sentinel.streamlit.app/)
    5. [Decentralized Storage Optimizer](https://rantai-greenstorage.streamlit.app/)
    6. [Cloud Carbon Footprint Tracker](https://rantai-greencloud.streamlit.app/)
    7. [Cloud.Climate.Chain](https://rantai-3c.streamlit.app/)
    8. [Property Management System](https://rantai-pms.streamlit.app/)
    
    🌱 Lab → “Grow the chain”
    1. [BlockBook](https://blockbook.streamlit.app/)
    2. [Data Insights & Visualization Assistant](https://rantai-diva.streamlit.app/)
    3. [Exploratory Data Analysis](https://rantai-exploda.streamlit.app/)
    4. [Business Intelligence](https://rantai-busi.streamlit.app/)
    5. [Predictive Modelling](https://rantai-model-predi.streamlit.app/)
    6. [Ethic & Bias Checker](https://rantai-ethika.streamlit.app/)
    7. [Smart Atlas For Environment](https://rantai-safe.streamlit.app/)
    8. [Blockchain Healthcare Revolution](https://healthchain.streamlit.app/)
    9. [Academic Flow Diagram Generator](https://mermaind.streamlit.app/)
    10. [Decentralized Agriculture](https://agroviz.streamlit.app/)
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

def embed_iframe(src, hide_top_px=100, hide_bottom_px=0, height=800):
    components.html(f"""
    <div style="height:{height}px; overflow:hidden; position:relative;">
        <iframe src="{src}" 
                style="width:100%; height:calc(100% + {hide_top_px + hide_bottom_px}px); border:none; position:relative; top:-{hide_top_px}px;">
        </iframe>
    </div>
    """, height=height + hide_top_px + hide_bottom_px)

# URL Ohara
iframe_url = "https://ohara.ai/mini-apps/9ae7b454-a3e4-47ba-ae7e-22b021377545"

# Panggil fungsi
embed_iframe(iframe_url, hide_top_px=110, hide_bottom_px = 80, height=800)
