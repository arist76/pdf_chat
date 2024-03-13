import { CONSTANTS } from '$lib/constants';
import axios from 'axios';
import { token } from '$lib/store';
import { get } from 'svelte/store';

const tokenVal = get(token);

const upVoteForum = async (slug: string) => {
	console.log('clicked')
	console.log(slug)
	const res = await axios.post(CONSTANTS.URL.FORUM + `${slug}` + '/upvote', {
		headers: {
			Authorization: `token ${tokenVal}`
		}
	});
	console.log(res)
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

export { upVoteForum, downVoteForum };
