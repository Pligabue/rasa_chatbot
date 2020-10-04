
def get_hours_util_estimation(occurrence):
    occurrence.time_until_estimation().total_seconds()//3600

def get_occurrence_messages(occurrence):
    return {
        "category": ("Uma manutenção" if occurrence.category_is("maintenance") else 
                     "Uma queda de energia" if occurrence.category_is("power_outage") else
                     "Um problema"),
        "status": ("está sendo feita" if occurrence.status_is("in_progress") and occurrence.category_is("maintenance") else
                   "está pendente" if occurrence.status_is("pending") and occurrence.category_is("maintenance") else
                   "está sendo investigada" if occurrence.status_is("in_progress") and occurrence.category_is("power_outage") else 
                   "ocorreu"),
        "estimation": "Ainda não há previsão de conclusão" if not occurrence.has_estimation() else
                      "A operação deve ser normalizada em menos de uma hora" if get_hours_util_estimation(occurrence) < 1 else
                      f"A operação deve ser normalizada dentro de {get_hours_util_estimation(occurrence)} hora{'s' if get_hours_util_estimation(occurrence) == 1 else ''}",
        "additional_comments": f"Para acompanhar o status da ocorrência, acesse sitegenerico.com/ocorrencia/{occurrence.id}."
    }