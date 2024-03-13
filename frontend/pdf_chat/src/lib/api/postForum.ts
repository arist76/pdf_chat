import { CONSTANTS } from '$lib/constants';
import axios from 'axios';
import { token } from '$lib/store';
import { get } from 'svelte/store';

const tokenVal = get(token);

const postForumAnswer = async ({ slug, text }: { slug: string; text: string | null }) => {
	console.log(tokenVal);
	try {
		const res = await axios.post(
			CONSTANTS.URL.FORUM + `${slug}/`,
			{
				text
			},
			{
				headers: {
					Authorization: `token ${tokenVal}`
				}
			}
		);
		console.log(res.data);
		return res.data;
	} catch (e) {
		console.log(e);
		return false;
	}
};

const upVoteForum = async (slug: string) => {
	const res = await axios.post(CONSTANTS.URL.FORUM + `${slug}` + '/upvote', {
		headers: {
			Authorization: `token ${tokenVal}`
		}
	});
	console.log(res);
	return res.data;
};

const downVoteForum = async (slug: string) => {
	const res = await axios.post(CONSTANTS.URL.FORUM + `${slug}` + '/downvote', {
		headers: {
			Authorization: `token ${tokenVal}`
		}
	});
	return res.data;
};

export { postForumAnswer, upVoteForum, downVoteForum };
