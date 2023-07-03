Special Functionalities
============================

.. TODO: change this italic view

Styling Methodology/Architecture
-------------------------------------

*	Problem: 
    In 2023 modern web era, atomic styling methodology is the dominant styling method, but there is one big problem in using this methodology which is using the right file extension while building these component, should I type styles using Vue or blade components?
*	Solution:
    Non of these was correct, but using both was the final choice, But this may led to code duplication (same logic will be typed twice in different languages) right? Yes of course this will led of code duplication in case of atomic styling architecture is not customized specially for this project. Atoms and molecules are styled using OOCSS tailwind styles and daisyUI package, which can be used without barriers in both blade and Vue components, Organisms will be typed using Vue components as they will not be used in server side rendered pages and pages layout will be created using blade components as they will be always server side rendered.

.. tip::
    Code standards are typed in detailed in docs folder in codebase to be able to differentiate between atoms, molecules, organisms and layouts. `Click here to view it <https://swagger.io/>`_ 

Exam handling – Frontend
---------------------------
* 	Problem:
    In case of accidentally browser refresh in exam page, all user’s answers will be lost, 
* 	Solution:
    IndexedDB client side storage is used to store exam data to avoid data loss, indexedDB is used instead of using local/session storage due to the need of storing structured data  (several pieces of info about each question with keys)

.. TODO:
sequence diagram here
