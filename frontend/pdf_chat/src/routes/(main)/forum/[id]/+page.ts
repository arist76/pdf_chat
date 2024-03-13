interface ParamsTypes {
	params: { id: string };
}
export function load({ params }: ParamsTypes) {
	return {
		post: {
			title: `Title for ${params.id} goes here`,
			content: `Content for ${params.id} goes here`
		}
	};
}
