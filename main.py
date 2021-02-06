from gelbooru import Post
import matplotlib.pyplot as plt

# post = Post.from_id(5867582)
# post2 = Post.from_id(4252737)
"""
characters = ["tokino_sora", "roboco-san", "sakura_miko", "akai_haato", "yozora_mel", "natsuiro_matsuri", "aki_rosenthal",
              "shirakami_fubuki", "oozora_subaru", "yuzuki_choco", "murasaki_shion", "nakiri_ayame", "minato_aqua",
              "ookami_mio", "nekomata_okayu", "inugami_korone", "azki_(hololive)", "hoshimachi_suisei", "usada_pekora",
              "uruha_rushia", "shiranui_flare", "shirogane_noel", "houshou_marine", "amane_kanata", "kiryuu_coco",
              "tsunomaki_watame", "himemori_luna", "tokoyami_towa", "yukihana_lamy", "momosuzu_nene", "shishiro_botan",
              "mano_aloe", "omaru_polka", "yogiri", "civia", "spade_echo", "doris_(hololive)", "artia",
              "rosalyn_(hololive)", "hanasaki_miyabi", "kagami_kira", "kanade_izuru", "yakushiji_suzaku", "arurandis",
              "rikka", "astel_leda", "kishidou_tenma", "yukoku_roberu", "ayunda_risu", "moona_hoshinova",
              "airani_iofifteen", "kureiji_ollie ", "anya_melfissa", "pavolia_reine", "mori_calliope", "takanashi_kiara",
              "ninomae_ina'nis", "gawr_gura", "amelia_watson", "yuujin_a_(hololive)", "yagoo"]

print(len(characters))

fig, axs = plt.subplots(8, 8, figsize=(32, 32))
"""

characters = ["shima_rin", "kagamihara_nadeshiko", "oogaki_chiaki", "inuyama_aoi", "saitou_ena", "kagamihara_sakura",
              "toba_minami", "toba_ryouko", "inuyama_akari"]
fig, axs = plt.subplots(3, 3)

ratings = ["rating:explicit", "rating:questionable", "rating:safe"]
labels = "Explicit", "Questionable", "Safe"
count = [0, 0, 0]

for ax, character in zip(axs.flat, characters):
    for i in range(3):
        _, count[i] = Post.search_tags(character, ratings[i])

    ax.set_title("Ratio of %s posts by rating" % character)
    ax.pie(count, labels=labels, autopct="%1.1f%%", shadow=True)
    ax.axis('equal')

    print("done with %s" % character, count)

for i in axs.flat[len(characters):]:
    i.set_visible(False)

fig.suptitle("hololive character image proportions on gelbooru")
plt.tight_layout()

plt.savefig("out.png")
plt.show()

# posts, _ = Post.search(tags="shima_rin rating:safe")


