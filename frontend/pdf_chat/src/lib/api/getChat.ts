import { CONSTANTS } from '$lib/constants';
import { token } from '$lib/store';
import axios from 'axios';
import { get } from 'svelte/store';

export const getChat = async (grade : string, subject : string) => {
	const tokenVal = get(token);
	const response = await axios.get(CONSTANTS.URL.CHAT, {
		headers: {
			Authorization: `token ${tokenVal}`
		},
		params : {
			chat__grade : grade,
			chat__subject : subject
		}
	});
	// console.log(response);
	return response.data;
};
