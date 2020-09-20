INDEX_SETTINGS = {
	'number_of_shards': 3,
	'number_of_replicas': 1,
	'refresh_interval': '5m',
	'analysis': {
		'analyzer': {
			'lowercaseonly': {
				'type': 'custom',
				'tokenizer': 'keyword',
				'filter': [
					'lowercase',
				]
			}
		},
		'normalizer': {
			'lowercaseonly': {
				'type': 'custom',
				'char_filter': [],
				'filter': [
					'lowercase',
				]
			},
		}
	}
}

DATA_MAPPING = {
	'_source': {
		'enabled': False,
	},
	'properties': {
		'pair': {
			'type': 'text',
			'fields': {
				'facet': {
					'type': 'keyword',
					'index': False,
				}
			}
		},
		'rate': {
			'type': 'float',
		},
		'created_at': {
			'type': 'float'
		}
	}
}
