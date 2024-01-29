from domino.base_piece import BasePiece
from .models import InputModel, OutputModel, SecretsModel
import requests
import base64
import json


class ReloadPiece(BasePiece):
     def piece_function(self, input_data: InputModel, secrets_data: SecretsModel):
        try:
            url = f'{secrets_data.TENANT_URL}/api/v1/reloads'
            headers = {'Authorization': f'Bearer {secrets_data.BEARER_TOKEN}'}
            body = json.dumps({"appId": input_data.app_id})
            response = requests.post(url, headers=headers, data=body)
            response.raise_for_status()
        except requests.RequestException as e:
            raise Exception(f'HTTP request error: {e}')
        return OutputModel(message=f'{input_data.app_id} reloded successfully.')
