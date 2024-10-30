import art
from translate import Translator

print(art.art("woman"))
print(art.text2art("test", "random"))

translator= Translator(to_lang="de")
translation = translator.translate("This is a pen.")

print(translation)


