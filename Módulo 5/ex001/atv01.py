import db1.helpers.strings #importa apenas o arquivo string que está dentro de helpers, dentro de db1

result = db1.helpers.strings.mask_cpf('12345678901')

print(result)