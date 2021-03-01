![LUSID_by_Finbourne](https://content.finbourne.com/LUSID_repo.png)
[![FOSSA Status](https://app.fossa.com/api/projects/git%2Bgithub.com%2Ffinbourne%2Flusid-jam.svg?type=shield)](https://app.fossa.com/projects/git%2Bgithub.com%2Ffinbourne%2Flusid-jam?ref=badge_shield)

Use within a LUSID hosted Jupyter notebook as follows: 

```
import os
from lusid.utilities import ApiClientFactory
from lusidjam import RefreshingToken as rt

api_factory = ApiClientFactory(token=rt.RefreshingToken(), api_url=os.getenv("FBN_LUSID_API_URL", None), app_name="Jupyter")
```

`$ pip install lusid-jam`


## License
[![FOSSA Status](https://app.fossa.com/api/projects/git%2Bgithub.com%2Ffinbourne%2Flusid-jam.svg?type=large)](https://app.fossa.com/projects/git%2Bgithub.com%2Ffinbourne%2Flusid-jam?ref=badge_large)