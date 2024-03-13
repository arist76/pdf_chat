import { getForumDeatil } from '$lib/api/getForums';
import type { ForumDetailTypes } from '../../../../types';

interface ParamsTypes {
	params: { slug: string };
}
export async function load({ params }: ParamsTypes) {
	const forum: ForumDetailTypes[] = await getForumDeatil(params.slug);
	return {
		forum
	};
}
