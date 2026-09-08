# Images

Types:

```python
from getimg.types import Usage, ImageGenerateResponse
```

Methods:

- <code title="post /v2/images/generations">client.images.<a href="./src/getimg/resources/images.py">generate</a>(\*\*<a href="src/getimg/types/image_generate_params.py">params</a>) -> <a href="./src/getimg/types/image_generate_response.py">ImageGenerateResponse</a></code>

# Videos

## Generations

Types:

```python
from getimg.types.videos import GenerationCreateResponse, GenerationRetrieveResponse
```

Methods:

- <code title="post /v2/videos/generations">client.videos.generations.<a href="./src/getimg/resources/videos/generations.py">create</a>(\*\*<a href="src/getimg/types/videos/generation_create_params.py">params</a>) -> <a href="./src/getimg/types/videos/generation_create_response.py">GenerationCreateResponse</a></code>
- <code title="get /v2/videos/generations/{id}">client.videos.generations.<a href="./src/getimg/resources/videos/generations.py">retrieve</a>(id) -> <a href="./src/getimg/types/videos/generation_retrieve_response.py">GenerationRetrieveResponse</a></code>

# Models

Types:

```python
from getimg.types import DeveloperModelRate, ModelRetrieveResponse, ModelListResponse
```

Methods:

- <code title="get /v2/models/{model}">client.models.<a href="./src/getimg/resources/models.py">retrieve</a>(model) -> <a href="./src/getimg/types/model_retrieve_response.py">ModelRetrieveResponse</a></code>
- <code title="get /v2/models">client.models.<a href="./src/getimg/resources/models.py">list</a>(\*\*<a href="src/getimg/types/model_list_params.py">params</a>) -> <a href="./src/getimg/types/model_list_response.py">ModelListResponse</a></code>

# Billing

Types:

```python
from getimg.types import BillingListCostsResponse, BillingRetrieveBalanceResponse
```

Methods:

- <code title="get /v2/billing/costs">client.billing.<a href="./src/getimg/resources/billing.py">list_costs</a>(\*\*<a href="src/getimg/types/billing_list_costs_params.py">params</a>) -> <a href="./src/getimg/types/billing_list_costs_response.py">BillingListCostsResponse</a></code>
- <code title="get /v2/billing/balance">client.billing.<a href="./src/getimg/resources/billing.py">retrieve_balance</a>() -> <a href="./src/getimg/types/billing_retrieve_balance_response.py">BillingRetrieveBalanceResponse</a></code>
