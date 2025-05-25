import requests

API_PRINCIPAL_URL = "http://localhost:8000/api/professores"

class ProfessorServiceClient:
    @staticmethod
    def verificar_professor(id_professor):
        try:
            response = requests.get(f"{API_PRINCIPAL_URL}/{id_professor}")
            return response.status_code == 200
        except requests.RequestException:
            return False
