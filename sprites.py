from pathlib import Path

grafikk_path = Path(__file__).resolve().parent
grafikk_path = grafikk_path / "Grafikk"

pritaskip_path = grafikk_path / "Pirat_spiller"
piratskip1_path = pritaskip_path / 'Piratskip1.png'
piratskip0_path = pritaskip_path / 'Piratskip0.png'
piratskipm1_path = pritaskip_path / 'Piratskip-1.png'

squid_path = grafikk_path / "Blekksprut"
squido0_path = squid_path / "squid0.png"
squido1_path = squid_path / "squid1.png"
squid_dykk1_path = squid_path / "squid_dykk1.png"
squid_dykk2_path = squid_path / "squid_dykk2.png"
squid0u_path = squid_path / "squid1(under).png"
squid1u_path = squid_path / "squid2(under).png"
squid2u_path = squid_path / "squid3(under).png"

shark_path = grafikk_path / "Shark"
sharkL2u_path = shark_path / "sharkL2(under).png"
sharkL1u_path = shark_path / "sharkL1(under).png"
shark0u_path = shark_path / "shark0(under).png"
sharkR1u_path = shark_path / "sharkR1(under).png"
sharkR2u_path = shark_path / "sharkR2(under).png"

sharkL2o_path = shark_path / "sharkL2(over).png"
sharkL1o_path = shark_path / "sharkL1(over).png"
shark0o_path = shark_path / "shark0(over).png"
sharkR1o_path = shark_path / "sharkR1(over).png"
sharkR2o_path = shark_path / "sharkR2(over).png"

pirat_sprites = [piratskip1_path, piratskip0_path, piratskipm1_path, piratskip0_path]
squido_sprites = [squido0_path, squido1_path, squido0_path, squido1_path]
squid_dykk_sprites = [squid_dykk1_path, squid_dykk2_path, squid_dykk1_path, squid_dykk2_path]
squid_opp_sprites = [squid_dykk2_path, squid_dykk1_path, squid_dykk2_path, squid_dykk1_path]
squidu_sprites = [squid0u_path, squid1u_path, squid2u_path, squid1u_path]
sharku_sprites = [sharkR1u_path, sharkR2u_path, sharkR1u_path, shark0u_path, sharkL1u_path, sharkL2u_path, sharkL1u_path,shark0u_path]
sharko_sprites = [sharkR1o_path, sharkR2o_path, sharkR1o_path, shark0o_path, sharkL1o_path, sharkL2o_path, sharkL1o_path, shark0o_path]