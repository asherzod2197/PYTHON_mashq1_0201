def baho_tahlil(baholar):
    orta = sum(baholar) / len(baholar)
    if orta >= 80:
        natija = "Yaxshi"
    elif orta >= 60:
        natija = "Qoniqarli"
    else:
        natija = "Yomon"
    return orta, natija


baholar = [75, 82, 68, 90]
orta, natija = baho_tahlil(baholar)
print("O‘rtacha:", orta)
print("Natija:", natija)
