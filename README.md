# S3 Image Resizer API

API Flask para redimensionar e otimizar imagens armazenadas no AWS S3. Utiliza Pillow para compressão de imagens e Boto3 para interação com o serviço de armazenamento S3 da AWS.

## Funcionalidades

- Baixar uma imagem do bucket S3
- Redimensionar a imagem mantendo a proporção
- Fazer o upload da imagem redimensionada de volta ao S3

## Tecnologias Utilizadas

- Python 3.x
- Flask
- Boto3 (SDK da AWS)
- Pillow (para manipulação de imagens)

## Instalação

1. Clone o repositório:

   ```bash
   git clone git@github.com:sousaprogramador/flask-s3-image-optimizer.git
   ```

2. Navegue até o diretório do projeto:

   ```bash
   cd flask-s3-image-optimizer.git
   ```

3. Crie e ative um ambiente virtual (opcional, mas recomendado):

   ```bash
   python -m venv venv
   source venv/bin/activate   # No Windows use: venv\Scripts\activate
   ```

4. Instale as dependências do projeto:

   ```bash
   pip install -r requirements.txt
   ```

5. Certifique-se de configurar suas credenciais da AWS (usando o arquivo `~/.aws/credentials` ou variáveis de ambiente).

## Uso

1. Inicie o servidor Flask:

   ```bash
   python app.py
   ```

2. Use a API para redimensionar uma imagem armazenada no AWS S3. Faça uma requisição `POST` para o endpoint `/reduce-image-size`:

   - **URL**: `http://localhost:5000/reduce-image-size`
   - **Método**: `POST`
   - **Body** (JSON):
     ```json
     {
       "bucket_name": "nome-do-bucket",
       "image_key": "caminho/para/a/imagem.jpg",
       "new_image_key": "caminho/para/nova/imagem.jpg",
       "max_size": [800, 600]
     }
     ```
   - **Resposta**:
     ```json
     {
       "message": "Image resized and uploaded successfully!"
     }
     ```

## Dependências

As dependências estão listadas no arquivo `requirements.txt`:

- Flask
- Pillow
- Boto3

## Contribuição

1. Faça um fork do projeto.
2. Crie uma branch para sua feature (`git checkout -b feature/nova-feature`).
3. Faça commit das suas alterações (`git commit -m 'Adiciona nova feature'`).
4. Envie a sua branch (`git push origin feature/nova-feature`).
5. Abra um Pull Request.

## Licença

Este projeto está licenciado sob os termos da [MIT License](LICENSE).
