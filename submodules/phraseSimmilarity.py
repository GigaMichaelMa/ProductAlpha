# Testing code, not what should be in the final module.


from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer
headlines = [
    # Crypto
    'Investors unfazed by correction as crypto funds see $154 million inflows',
    'Bitcoin, Ethereum prices continue descent, but crypto funds see inflows',

    # Inflation
    'The surge in euro area inflation during the pandemic: transitory but with upside risks',
    "Inflation: why it's temporary and raising interest rates will do more harm than good",

    # common
    'Will Cryptocurrency Protect Against Inflation?']


labels = [headline[:20] for headline in headlines]


def create_heatmap(similarity, cmap="YlGnBu"):
    df = pd.DataFrame(similarity)
    df.columns = labels
    df.index = labels
    fig, ax = plt.subplots(figsize=(5, 5))
    sns.heatmap(df, cmap=cmap)


vectorizer = CountVectorizer()
X = vectorizer.fit_transform(headlines)
arr = X.toarray()

create_heatmap(cosine_similarity(arr))
