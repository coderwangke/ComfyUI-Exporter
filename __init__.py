from collector.py import collector

NODE_CLASS_MAPPINGS = {
    "PrometheusCollector": collector
}
__all__ = ['NODE_CLASS_MAPPINGS']
