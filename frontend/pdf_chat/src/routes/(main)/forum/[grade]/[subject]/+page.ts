import { getForums } from '$lib/api/getForums';
import type { ForumDataTypes } from '../../../types';

interface ParamsTypes {
	params: { grade: string; subject: string };
}

export async function load({ params }: ParamsTypes) {
	const forums: ForumDataTypes[] = await getForums({ subject: params.subject, grade: params.grade });
	return {
		forums: forums
	};
}
