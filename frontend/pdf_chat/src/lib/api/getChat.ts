import { CONSTANTS } from '$lib/constants';
import { authToken } from '$lib/store';
import axios from 'axios';
import { get } from 'svelte/store';

export const getChat = async () => {
	const token = get(authToken);
	const response = await axios.get(CONSTANTS.URL.CHAT, {
		headers: {
			Authorization: `token ${token}`
		}
	});
	// console.log(response);
	return response.data;
};
