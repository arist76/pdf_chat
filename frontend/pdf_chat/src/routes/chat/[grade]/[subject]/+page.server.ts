import type { PageServerLoad  } from './$types';

export const load : PageServerLoad  = async ({ cookies, params }) => {
    cookies.set("grade", params.grade, {
        httpOnly: false,
        sameSite: 'none',
        path: '/',
    })
    cookies.set("subject", params.subject, {
        httpOnly: false,
        sameSite: 'none',
        path: '/',
    })
            
}