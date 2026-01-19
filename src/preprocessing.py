from sklearn.preprocessing import StandardScaler,OneHotEncoder
from sklearn.compose import ColumnTransformer
from config import NUM_FEATURES, CAT_FEATURES

def build_preprocessor():

    num_transformer = StandardScaler()
    cat_transformer = OneHotEncoder(handle_unknown="ignore")

    preprocessor = ColumnTransformer(
        transformers= [
            ("num",num_transformer, NUM_FEATURES),
            ("cat",cat_transformer, CAT_FEATURES)
        ]
    )
    return preprocessor


