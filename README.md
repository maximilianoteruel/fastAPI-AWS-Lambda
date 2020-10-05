# FastAPI

Generate Migration:

```bash
alembic revision --autogenerate -m "name"

```

Run Tests:

```bash
 pytest --cov=app --cov-report=term-missing:skip-covered app/tests
```

Deploy on AWS Lambda:

```bash
sam validate

sam build --use-container --debug

sam package --s3-bucket fast-api-bucket  --output-template-file out.yml --region sa-east-1

sam deploy --template-file out.yml --stack-name STACKIS --region sa-east-1 --no-fail-on-empty-changeset --capabilities CAPABILITY_IAM
```
