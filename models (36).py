/* ================= RESET ================= */
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
    font-family: Arial;
}

body {
    background: #f3f6fb;
    margin: 0;
    padding: 0;
}

/* ================= NAVBAR ================= */
.navbar {
    position: sticky;
    top: 0;
    z-index: 1000;

    display: flex;
    justify-content: space-between;
    align-items: center;

    padding: 12px 20px;
    background: white;

    box-shadow: 0 5px 20px rgba(0, 0, 0, 0.05);

    animation: slideDown 0.4s ease;
}

@keyframes slideDown {
    from {
        transform: translateY(-50px);
        opacity: 0;
    }

    to {
        transform: translateY(0);
        opacity: 1;
    }
}

.logo {
    font-size: 20px;
    font-weight: bold;
}

.nav-links a {
    margin: 0 10px;
    text-decoration: none;
    color: #333;
    transition: 0.3s;
}

.nav-links a:hover {
    color: green;
    transform: scale(1.1);
}

/* ================= USER ================= */
.user-box {
    position: relative;
}

.nav-avatar {
    width: 42px;
    height: 42px;
    border-radius: 50%;
    object-fit: cover;
    border: 2px solid #ddd;
    cursor: pointer;
    transition: 0.3s;
}

.nav-avatar:hover {
    transform: scale(1.15) rotate(3deg);
}

/* DROPDOWN */
.dropdown {
    display: none;
    position: absolute;
    right: 0;
    top: 55px;
    background: white;
    border-radius: 10px;
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
    overflow: hidden;
    min-width: 160px;
}

.dropdown a {
    display: block;
    padding: 10px;
    color: #333;
    text-decoration: none;
    transition: 0.2s;
}

.dropdown a:hover {
    background: #f0f0f0;
}

/* ================= LAYOUT ================= */
.layout {
    display: grid;
    grid-template-columns: 1fr 2.5fr 1fr;
    gap: 15px;
    padding: 20px;
}

/* ================= LEFT ================= */
.left {
    background: white;
    padding: 15px;
    border-radius: 15px;

    height: fit-content;
    position: sticky;
    top: 80px;

    animation: fadeIn 0.5s ease;
}

.left a {
    display: block;
    margin: 10px 0;
    color: #333;
    text-decoration: none;
    transition: 0.2s;
}

.left a:hover {
    color: green;
    transform: translateX(5px);
}

.user-card {
    padding: 8px;
    border-bottom: 1px solid #eee;
    display: flex;
    gap: 8px;
    align-items: center;
}

.dot {
    width: 8px;
    height: 8px;
    border-radius: 50%;
    background: green;
}

/* ================= CENTER ================= */
.center {
    display: flex;
    flex-direction: column;
    gap: 12px;
}

/* POST CREATE */
.create-post {
    background: white;
    padding: 15px;
    border-radius: 12px;
    cursor: pointer;
    transition: 0.3s;
}

.create-post:hover {
    transform: scale(1.02);
}

/* POST */
.post {
    background: white;
    padding: 15px;
    border-radius: 15px;

    transition: 0.3s;
    animation: fadeIn 0.5s ease;
}

.post:hover {
    transform: translateY(-5px);
    box-shadow: 0 10px 25px rgba(0, 0, 0, 0.08);
}

.post-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
}

.post-user {
    display: flex;
    align-items: center;
    gap: 10px;
}

.post-avatar {
    width: 40px;
    height: 40px;
    border-radius: 50%;
    object-fit: cover;
}

.post-time {
    font-size: 12px;
    color: gray;
}

.post-body {
    margin-top: 10px;
    font-size: 14px;
    line-height: 1.5;
}

.post-actions {
    margin-top: 10px;
    display: flex;
    gap: 10px;
}

.post-actions button {
    border: none;
    padding: 6px 10px;
    border-radius: 8px;
    cursor: pointer;
    background: #f0f0f0;
    transition: 0.2s;
}

.post-actions button:hover {
    background: green;
    color: white;
}

/* ================= RIGHT ================= */
.right {
    background: white;
    padding: 15px;
    border-radius: 15px;

    height: fit-content;
    position: sticky;
    top: 80px;
}

.trend {
    padding: 8px;
    border-bottom: 1px solid #eee;
}

/* ================= FLOAT BUTTON ================= */
.float-btn {
    position: fixed;
    bottom: 25px;
    right: 10px;

    width: 45px;
    height: 45px;

    background: aqua;
    color: white;
    font-size: 50px;

    border-radius: 50%;

    display: flex;
    align-items: center;
    justify-content: center;

    cursor: pointer;

    box-shadow: 0 10px 25px rgba(0, 0, 0, 0.2);
    transition: 0.3s;
}

.float-btn:hover {
    transform: scale(1.1);
}

/* ================= MODAL ================= */
.modal {
    display: none;
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;

    background: rgba(0, 0, 0, 0.5);

    justify-content: center;
    align-items: center;

    animation: fadeIn 0.3s ease;
}

.modal-box {
    background: white;
    padding: 20px;
    border-radius: 15px;
    width: 320px;
}

/* ================= ANIMATION ================= */
@keyframes fadeIn {
    from {
        opacity: 0;
        transform: translateY(10px);
    }

    to {
        opacity: 1;
        transform: translateY(0);
    }
}

/* ================= MOBILE ================= */
@media (max-width: 900px) {

    .layout {
        grid-template-columns: 1fr;
    }

    .left,
    .right {
        display: none;
    }

    .create-post {
        font-size: 14px;
    }
}

.admin-link {
    display: none;

}

.admin-link::after {
    content: "";
    position: absolute;
    left: 0;
    bottom: -3px;
    width: 0%;
    height: 2px;
    background: red;
    transition: 0.3s;
}

.admin-link:hover::after {
    width: 100%;
}

.down-box {
    height: 50px;
    background: white;
    flex: 1;
    box-sizing: border-box;
    margin: 35px 70px;
    transition: 0.3s;
    border-radius: 30px;
    box-shadow: 0 4px 20px rgba(0,0,0,0.08);
    position: sticky;
    z-index:-9999;
}

.news-box {
    background: white;
    padding: 200px;
    border-radius: 12px;
    transition: 0.3s;
}