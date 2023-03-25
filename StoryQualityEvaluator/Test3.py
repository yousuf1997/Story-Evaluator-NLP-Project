from utills.EntityRemoverUtill import EntityRemoverUtill

utill = EntityRemoverUtill()

sentences = [
    "I worked at NASA for long time.",
    "Cuba is a great place to visit.",
    "Abraham Lincoln is great president river."
]

sentences = utill.removeEntities(sentences)

print(sentences)




