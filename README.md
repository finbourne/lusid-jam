![LUSID_by_Finbourne](./resources/Finbourne_Logo_Teal.svg)

Use within a LUSID hosted Jupyter notebook as follows: 

```
import os
from lusid.utilities import ApiClientFactory
from lusidjam import RefreshingToken as rt

api_factory = ApiClientFactory(token=rt.RefreshingToken(), api_url=os.getenv("FBN_LUSID_API_URL", None), app_name="Jupyter")
```

`$ pip install lusid-jam`
