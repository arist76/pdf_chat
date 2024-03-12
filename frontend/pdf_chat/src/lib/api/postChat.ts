import { CONSTANTS } from '$lib/constants';
import { token } from '$lib/store';
import axios from 'axios';
import { get } from 'svelte/store';

export const postChat = async (text: string) => {
	const tokenVal = get(token)

    // TODO: MAKE FORM DATA DYNAMIC
	const response = await axios.post(
		CONSTANTS.URL.CHAT,
		{
			chat: {
				subject: 'biology',
				grade: '9'
			},
			text
		},
		{
			headers: {
				Authorization: `token ${tokenVal}`
			}
		}
	);
	console.log(response.data);
	return response.data;
};
