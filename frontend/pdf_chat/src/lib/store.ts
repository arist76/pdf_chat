import { writable, type Writable } from 'svelte/store';
import { getCookieValue } from './utils';

// stores
export const token: Writable<null | string> = writable(null);

// TODO: make userInfo Dynamic
export const userInfo: Writable<{ grade: number; subject: string }> = writable({
	grade: 9,
	subject: 'biology'
});

// initialize stores
// On client side, update token with the value from cookie
if (typeof window !== 'undefined') {
	const initialToken = getCookieValue('auth_token');
	if (initialToken) {
		token.set(initialToken);
	}
}
