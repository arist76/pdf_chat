import { CONSTANTS } from '$lib/constants';
import { authToken } from '$lib/store';
import axios from 'axios';
import { get } from 'svelte/store';

export const getChat = async (grade : string, subject : string) => {
	const token = get(authToken);
	const response = await axios.get(CONSTANTS.URL.CHAT, {
		headers: {
			Authorization: `token ${token}`
		},
		params : {
			chat__grade : grade,
			chat__subject : subject
		}
	});
	// console.log(response);
	return response.data;
};
