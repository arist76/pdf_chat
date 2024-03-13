import { CONSTANTS } from '$lib/constants';
import axios from 'axios';
import { token } from '$lib/store';
import { get } from 'svelte/store';

const tokenVal = get(token);

const getForums = async ({ subject, grade }: { subject: string; grade: string }) => {
	const res = await axios.get(CONSTANTS.URL.FORUM, {
		headers: {
			Authorization: `token ${tokenVal}`
		},
		params: {
			subject,
			grade
		}
	});
	return res.data;
};

const getForumDeatil = async (slug: string) => {
	const res = await axios.get(CONSTANTS.URL.FORUM + `${slug}`, {
		headers: {
			Authorization: `token ${tokenVal}`
		}
	});
	console.log(res.data);
	return res.data;
};

export { getForums, getForumDeatil };
