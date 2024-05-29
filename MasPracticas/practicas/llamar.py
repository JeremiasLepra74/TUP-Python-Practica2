def validar_numero_documento(medicos: list, dni:str) -> bool:
    return any(medico["dni"] == dni for medico in medicos)  