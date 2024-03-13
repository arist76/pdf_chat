interface ForumDataTypes {
	id: number;
	title: string;
	title_slug: string;
	description: string;
	subject: string;
	grade: string;
	owner: number;
}

interface ForumDetailTypes {
    id: number;
    text: string;
    date: string; 
    upvotes: number;
    downvotes: number;
    room: number;
    user: number;
}
export { ForumDataTypes , ForumDetailTypes};
