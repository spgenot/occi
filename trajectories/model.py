from sklearn.cluster import DBSCAN

__author__ = 'spgenot'


class DBScan:
    """
    DBScan model.
    """
    def __init__(self, features, eps, min_samples):
        """
        Initialisation method for DBScan
        :param features: trajectory feature to learn from
        :type features: list()
        """
        self.features = features
        self.model = DBSCAN(eps=eps, min_samples=min_samples)
        self.cluster_labels = []

    def fit_predict(self):
        """
        Fits the model to the data and return the cluster labels.
        """
        self.cluster_labels = self.model.fit_predict(self.features)

