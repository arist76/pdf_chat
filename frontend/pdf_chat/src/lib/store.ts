import { writable, type Writable } from 'svelte/store';

export const token: Writable<null | string> = writable(null);
