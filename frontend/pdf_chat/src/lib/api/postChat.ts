import { CONSTANTS } from '$lib/constants';
import { authToken } from '$lib/store';
import axios from 'axios';
import { get } from 'svelte/store';

export const postChat = async ({text, grade, subject}:{text:string,grade:string,subject:string}) => {
		
	console.log(grade, subject)
	
	const token = get(authToken)

    // TODO: MAKE FORM DATA DYNAMIC
	const response = await axios.post(
		CONSTANTS.URL.CHAT,
		{
			chat: {
				subject: subject,
				grade: grade
			},
			text
		},
		{
			headers: {
				Authorization: `token ${token}`
			}
		}
	);
	console.log(response.data);
	return response.data;
};
