def forward_chaining(gejala_user, rules):
    for rule in rules:
        if all(g in gejala_user for g in rule["gejala"]):
            return rule["penyakit"], rule["saran"]
    return "Penyakit tidak teridentifikasi", "Silakan konsultasi ke dokter."
