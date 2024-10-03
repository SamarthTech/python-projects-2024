from sklearn.metrics.pairwise import cosine_similarity

def calculate_similarity(query_features, reference_features):
    print("Query features shape:", query_features.shape)
    print("Reference features shape:", reference_features.shape)
    
    # Check dimensions and transpose if necessary
    if query_features.shape[1] != reference_features.shape[1]:
        reference_features = reference_features.T
    
    # Check dimensions again after potential transposition
    if query_features.shape[1] != reference_features.shape[1]:
        raise ValueError("Incompatible dimensions for query and reference features")
    
    similarity_scores = cosine_similarity(query_features, reference_features)
    return similarity_scores
