Tech stack
============ 
Here are list points to discuss why each tech is chosen carefully.


Main tiers
------------

*	Backend: Laravel
    *   Laravel web application framework is used in this website as handling almost all of the business logic, APIs, authentication and authorization heavy duties in Laravel is pretty straight forwards. This website is mainly a backend project and Laravel is the best choice for this case.
    *	Laravel or PHP scripting language generally is chosen according to developer preference to gain PHP experience.
*	Frontend: Laravel / Vue
    *	Laravel is used to build server side rendered pages in only some specific pages that SEO is a must for it.
    *	Vue is used to build the whole application after the user is signed in to take the advantage of robust JavaScript packages and it is used mainly to build exam SPA (single page application) to provide superb exam experience for the user even if there is internet connection interruption.
*	Database: MySQL

Frontend details
-----------------
    *	Styling: tailwind
    *	Tailwind is used to take the advantage of using pre-built tailwind components due to the lack of UX UI design existence.
    *	Tailwind is mainly used to handle styling strategy that is explained in details here.
    *	State management: Pinia
    *	Client side requests: Axios

Backend details
-----------------
    *	Authentication & Authorization: Stateful session cookies & stateful Sanctum tokens

Others
-----------------
    *	Build tool: Vite 
    *	The main reason is that Vite has proved better browser load in small/mid website
    *	ORM: Eloquent
    *	The official Laravel ORM

