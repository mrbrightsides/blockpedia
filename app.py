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
    ### 🧩 Apps Showcase
    Lihat disini untuk semua tools yang kami kembangkan:
    [ELPEEF](https://showcase.elpeef.com/)
    
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

import streamlit.components.v1 as components

def embed_iframe(src, hide_top_px=100, hide_bottom_px=0, height=800):
    components.html(f"""
    <style>
        @media (max-width: 768px) {{
            .hide-on-mobile {{
                display: none !important;
            }}
            .show-on-mobile {{
                display: block !important;
                padding: 24px 12px;
                background: #ffecec;
                color: #d10000;
                font-weight: bold;
                text-align: center;
                border-radius: 12px;
                font-size: 1.2em;
                margin-top: 24px;
                animation: fadeIn 0.6s ease-in-out;
                box-shadow: 0 4px 12px rgba(0,0,0,0.2);
            }}
        }}
        @media (min-width: 769px) {{
            .show-on-mobile {{
                display: none !important;
            }}
        }}
        @keyframes fadeIn {{
            from {{ opacity: 0; transform: translateY(12px); }}
            to {{ opacity: 1; transform: translateY(0); }}
        }}
    </style>

    <!-- Desktop view -->
    <div class="hide-on-mobile" style="height:{height}px; overflow:hidden; position:relative;">
        <iframe src="{src}" 
                style="width:100%; height:calc(100% + {hide_top_px + hide_bottom_px}px); 
                       border:none; position:relative; top:-{hide_top_px}px;">
        </iframe>
    </div>

    <!-- Mobile fallback -->
    <div class="show-on-mobile">
        📱 Tampilan ini tidak tersedia di perangkat seluler.<br>
        Silakan buka lewat laptop atau desktop untuk pengalaman penuh 💻
    </div>
    """, height=height + hide_top_px + hide_bottom_px)

# URL Ohara
iframe_url = "https://blockpedia.elpeef.com/"

# Panggil fungsi
embed_iframe(iframe_url, hide_top_px=110, hide_bottom_px = 25, height=800)
